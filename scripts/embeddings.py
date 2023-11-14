import openai
import pandas as pd
from configparser import ConfigParser

#Read configuration from a Config file 
config = ConfigParser()
config.read('config.ini')
openai.api_type = "azure"
openai.api_key = config.get('Azure OpenAI','api_key')
openai.api_base = config.get('Azure OpenAI','api_base')
openai.api_version = "2023-05-15"

# Load your dataset from CSV
file_path = "train_data.csv"
df = pd.read_csv(file_path)
embeddings = []
# Generate embeddings for the column descriptions
for description in df["Description"]:
    response = openai.Embedding.create(input=description, engine="text-embedding-ada-002")
    if 'data' in response and response['data'] and 'embedding' in response['data'][0]:
        embeddings.append(tuple(response['data'][0]['embedding']))
    else:
        print(f"Error processing description: {description}")
        print(response)

# Add the embeddings to the DataFrame
df['Embedding'] = embeddings

# Save the DataFrame to a new CSV file with embeddings
df.to_csv("embeddings_data.csv", index=False)