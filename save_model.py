import pandas as pd
import os
import pickle
# Load embeddings from the pre-generated CSV file
embedding_df = pd.read_csv("embeddings_data.csv")
embedding_csv_file = "embeddings_data.csv"

if not os.path.isfile(embedding_csv_file):
    print(f"Embeddings CSV file ({embedding_csv_file}) does not exist. Please run generate_embeddings.py first.")
    exit()

embeddings = embedding_df['Embedding'].apply(eval)
# Create a dictionary of embeddings and corresponding (command, link) pairs
embedding_dict = {embedding: (embedding_df.loc[i, "Command"], embedding_df.loc[i, "Link"]) for i, embedding in enumerate(embeddings)}
embedding_dict_file = "aos10.pkl"
with open(embedding_dict_file, 'wb') as file:
        pickle.dump(embedding_dict, file)