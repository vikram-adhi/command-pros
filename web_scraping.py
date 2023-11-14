import argparse
import os
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument(f"--user-agent={my_user_agent}")

#get commands and respective links from the website and save it to csv
def scrape_data(web_path, command_path):
    wd = webdriver.Chrome(options=options)
    wd.get(web_path)

    try:
        # Wait for the dynamic content to load
        WebDriverWait(wd, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'tree-node-leaf'))
        )

        #sleep to wait for content to load
        time.sleep(2)

        # Extract the content
        all_elements = wd.find_elements(By.CLASS_NAME, 'tree-node-leaf')
        # Create a CSV file and write header
                                    
        with open(command_path, 'w+', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Command', 'Link']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for element in all_elements:
                command_text = element.text
                if(command_text!=''):
                    link = element.find_element(By.TAG_NAME, 'a').get_attribute('href')

                    writer.writerow({'Command': command_text, 'Link': link})

    finally:
        wd.quit()

#Navitage to all links from csv and collect the Description and save it to csv
def update_description(command_path, embeddings_path):
    wd = webdriver.Chrome(options=options)

    try:
        # Read commands and links from the CSV file
        with open(command_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

            # Create a new CSV file to store the updated information
            with open(embeddings_path, 'w', newline='', encoding='utf-8') as output_csvfile:
                fieldnames = ['Command', 'Link', 'Description']
                writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in rows:
                    command_text = row['Command']
                    link = row['Link']
                    wd.get(link)

                    try:
                        # Extract the description from the webpage
                        description_element = WebDriverWait(wd, 10).until(
                            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Description')]/following-sibling::p"))
                        )
                        description_text = description_element.text
                    except Exception as e:
                        print(f"An error occurred while extracting description for {command_text}: {e}")
                        description_text = "Description extraction failed."

                    # Write command, link, and description to the new CSV file
                    writer.writerow({'Command': command_text, 'Link': link, 'Description': description_text})

    finally:
        wd.quit()


def main():
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="input your Aruba CLI command website and the output path")
    parser.add_argument("website", help="Input your website URL of Aruba CLI")
    parser.add_argument("output_path", help="output folder path save the scrapped data along with embeddings")
    args = parser.parse_args()
    command_path = os.path.join(args.output_path, "command.csv")
    embeddings_path = os.path.join(args.output_path, "command_desc.csv")

    scrape_data(args.website, command_path)
    update_description(command_path, embeddings_path)

if __name__ == "__main__":
    main()