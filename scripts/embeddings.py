import openai
import pandas as pd
from configparser import ConfigParser
import argparse
import os
import pickle
from tqdm import tqdm

#Read configuration from a Config file 
config = ConfigParser()
config.read('../config.ini')
openai.api_type = "azure"
openai.api_key = config.get('Azure OpenAI','api_key')
openai.api_base = config.get('Azure OpenAI','api_base')
openai.api_version = "2023-05-15"


def get_embeddings(df, output_path, output_path_pkl):
    embeddings = []
    # Generate embeddings for the column descriptions
    for description in tqdm(df['Preprocessed_Description'], desc="Generating Embeddings", unit="description"):
        response = openai.Embedding.create(input=description, engine="text-embedding-ada-002")
        if 'data' in response and response['data'] and 'embedding' in response['data'][0]:
            embeddings.append(tuple(response['data'][0]['embedding']))
        else:
            print(f"Error processing description: {description}")
            print(response)

    # Add the embeddings to the DataFrame
    df['Embedding'] = embeddings

    # Save the DataFrame to a new CSV file with embeddings
    df.to_csv(output_path, index=False)

    print('Saved the embeddings to a CSV file...')


    # Save the embeddings to a pickle file

    embedding_df = pd.read_csv(output_path)

    embeddings = embedding_df['Embedding'].apply(eval)
    # Create a dictionary of embeddings and corresponding (command, link) pairs
    embedding_dict = {embedding: (embedding_df.loc[i, "Command"], embedding_df.loc[i, "Link"]) for i, embedding in enumerate(embeddings)}
    with open(output_path_pkl, 'wb') as file:
            pickle.dump(embedding_dict, file)

def main():
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="input your file data path for the embedding and pkl file generation")
    parser.add_argument("folder_path", help="Input your dataset folder path")
    args = parser.parse_args()
    input_path = os.path.join(args.folder_path, "command_desc_preprocessed.csv")
    output_path = os.path.join(args.folder_path, "embedding_data.csv")
    output_path_pkl = os.path.join(args.folder_path, "embedding.pkl")
    df = pd.read_csv(input_path)
    get_embeddings(df, output_path, output_path_pkl)

    print("Generated embeddings...")

if __name__ == "__main__":
    main()