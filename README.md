# Revolutionizing Command Execution With Natural Text Retrieval 

#### [Tech-Con Hackathon Idea - D32854](https://hpe.brightidea.com/D32854)

# Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Runtime](#runtime)
5. [Steps to create environment](#steps-to-create-environment)
    - [config file creation](#creating-a-config-file)
    - [Backend](#backend---python-fastapi)
    - [Frontend](#frontend---angular)
    - [Embeddings Creation](#steps-to-collect-the-embeddings)
6. [Contacts Info](#contact-info)

---
## Overview

In today's fast-paced and technology-dependent world, efficiently managing a growing number of commands and instructions for various tasks is a challenge. The traditional methods of memorizing or referencing commands can be time-consuming, error-prone, and counterproductive. This project proposes the utilization of Open AI (GenAI) to simplify command retrieval and reduce the cognitive load associated with remembering specific instructions.

---
## Features

- **Command Retrieval:** Use Generative AI to generate commands based on user input.
- **Reduced Cognitive Load:** Simplify the process of recalling and executing commands for individual applications/OS.
---
## Technologies Used

Following are the technologies used in our project.

- Microsoft Azure OpenAI
- Python
- Fast API
- Angular
- Selenium

---
## Runtime

The following are the runtimes that can be used to execute the project.

- Python 3.10
- Node v14.16.1
- npm 6.14.12
- Operating System: MAC, Linux and Windows.

---

## Steps to create environment

Following are the steps that need to be followed for the programg execution.
- ## Creating a Config file
    - create a `config.ini` in your workspace.
    - Add your azure open ai API Key, endpoint URL and deployment app host, port.
    ```
    # Set your Azure OpenAI API endpoint, key and FastAPI host, port

    [Azure OpenAI]
    api_type = azure
    api_key = your_api_key
    api_base = your_endpoint_URL
    api_version = 2023-05-15

    [app]
    host = 127.0.0.1
    port = 8000
    ```
---

- ## Backend - Python FastAPI
    - Create a virtual environment in the root folder
        >`python -m venv env`
    - Activate the python environment 
        >`source env/bin/activate`
    - Install the python packages through requirements file.
        >`pip install -r requirement.txt`
    - To run the Fast API application,
        > `uvicorn main:app`

        By default, the application will run on [localhost:8000](http://localhost:8000/).
    
    - Once it has successfully run, you will be able to see the Swagger docs at [localhost:8000/docs](http://localhost:8000/).

        ![swagger](/img/swagger.png)
    - You can try the APIs from the play ground itself 🎉

- ## Frontend - Angular
    Time to use the User Interface.
    - Change the directory to `ui` and do npm install.
        >`cd ui`<br>
        >`npm install`
    - Serve the code.
        >`ng serve`
    - By default the UI application will run on [localhost:4200](http://localhost:4200/)
    - Now, you can able to see the UI for selecting the products (AOS10, Clear pass., etc) and the input text to put your query to retrieve the relevant command along with the description.
    ![ui](/img/ui.png)

    > Big burden of memorizing many commands got overcome with this tool. We hope frequent CLI users will have great impact with this product.


## Steps to collect the embeddings
- Set the URL of the commands page that you want to scrape.
    > The code is developed to scrape the command, link, descriptions of the [Aruba CLI Bank](https://www.arubanetworks.com/techdocs/CLI-Bank/Content/Home.htm)
- Run ```python web_scraping.py /dataset/<folder_name>``` to generate a CSV file containing command, link, and description, respectively.

- Run ```python preprocess.py /dataset/<folder_name>/command_desc.csv``` which will preprocess all the descriptions in the csv file
- Run ```python embeddings.py /dataset/<folder_name>/command_desc_preprocessed.csv``` which will generate new csv file containing with embeddings and stored them to pickle file.
--- 
## Contact Info

If you face any issue in setting up, kindly contact the TechCon Hackathon contributors. Feedback and suggestions are always welcome.

1. [Nithishkumar K R](nithishkumar.kuduva-ravi-sankar@hpe.com)
2. [Vikram Adithya](vikram-adithya-reddy.yataluru@hpe.com)
