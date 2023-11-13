import argparse
import pandas as pd
import openai
import os
from sklearn.metrics.pairwise import cosine_similarity
from configparser import ConfigParser

#Read configuration from a Config file 
config = ConfigParser()
config.read('config.ini')
openai.api_type = config.get('Azure OpenAI','api_type')
openai.api_key = config.get('Azure OpenAI','api_key')
openai.api_base = config.get('Azure OpenAI','api_base')
openai.api_version = config.get('Azure OpenAI','api_version')

# Load embeddings from the pre-generated CSV file
embedding_df = pd.read_csv("embeddings_data.csv")
embedding_csv_file = "embeddings_data.csv"

if not os.path.isfile(embedding_csv_file):
    print(f"Embeddings CSV file ({embedding_csv_file}) does not exist. Please run generate_embeddings.py first.")
    exit()

embeddings = embedding_df['Embedding'].apply(eval)
# Create a dictionary of embeddings and corresponding (command, link) pairs
embedding_dict = {embedding: (embedding_df.loc[i, "Command"], embedding_df.loc[i, "Link"]) for i, embedding in enumerate(embeddings)}

# Define a function to search for similar descriptions based on user input
def search_similar_descriptions(user_input):
    # Print the user input
    print(f"User input: {user_input}")
    resp = openai.Embedding.create(input=user_input, engine="text-embedding-ada-002")
    user_embedding = resp['data'][0]['embedding']

    most_similar_embedding = None
    max_similarity = 0
    for embedding, (command, link) in embedding_dict.items():
        similarity = cosine_similarity([embedding], [user_embedding])
        if similarity > max_similarity:
            most_similar_embedding = embedding
            max_similarity = similarity

    # Return the corresponding (command, link) pair
    return embedding_dict[most_similar_embedding]

def main():
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="Search for similar descriptions and get corresponding command and link.")
    parser.add_argument("user_input", help="User input description for search")
    args = parser.parse_args()
    result = search_similar_descriptions(args.user_input)

    if result:
        command, link = result
        print("Command:", command)
        print("Link:", link)

if __name__ == "__main__":
    main()