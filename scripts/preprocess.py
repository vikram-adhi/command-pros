import argparse
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import string
import os
import csv

nltk.download('punkt')
nltk.download('stopwords')

custom_stop_words = ["command", "displays", "purpose", "description"]
stop_words = set(stopwords.words('english') + custom_stop_words)

def preprocess_text(command, description):
    description = description.lower()

    tokens = word_tokenize(description)

    tokens = [token for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stop_words]

    # Joining tokens back into a string
    preprocessed_description = ' '.join(tokens)

    return command+" "+preprocessed_description


def main():
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="input your file data path for the preprocessed output")
    parser.add_argument("folder_path", help="Input your dataset folder path")
    args = parser.parse_args()
    input_path = os.path.join(args.folder_path, "command_desc.csv")
    output_path = os.path.join(args.folder_path, "command_desc_preprocessed.csv")
    
    df = pd.read_csv(input_path)

    df['Preprocessed_Description'] = df.apply(lambda row: preprocess_text(row['Command'], row['Description']), axis=1)
    # Save the updated DataFrame to the same CSV file
    
    selected_columns = ['Command', 'Link', 'Description', 'Preprocessed_Description']

    df_selected = df[selected_columns]
    df_selected.to_csv(output_path, index=False)

    print(df_selected.isna().sum())
    print("Preprocessing complete!")
if __name__ == "__main__":
    main()