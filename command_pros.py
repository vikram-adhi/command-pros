import argparse
import pandas as pd
import openai
import os
from sklearn.metrics.pairwise import cosine_similarity
from configparser import ConfigParser
import pickle
import time
from heapq import heappush, heappop

#Read configuration from a Config file 
config = ConfigParser()
config.read('config.ini')
openai.api_type = "azure"
openai.api_key = config.get('Azure OpenAI','api_key')
openai.api_base = config.get('Azure OpenAI','api_base')
openai.api_version ="2023-05-15"

embedding_dict_file = "./dataset/AOS10/embedding.pkl"

try:
    with open(embedding_dict_file, 'rb') as file:
        embedding_dict = pickle.load(file)
except FileNotFoundError:
    embedding_dict = {}

# Define a function to search for similar descriptions based on user input
def search_similar_descriptions(user_input):
    # Print the user input
    print(f"User input: {user_input}")
    start_time = time.time()
    resp = openai.Embedding.create(input=user_input, engine="text-embedding-ada-002")
    user_embedding = resp['data'][0]['embedding']
    end_time = time.time()
    most_similar_embedding = None
    max_similarity = 0

    top3_heap = []

    # Iterate through each embedding
    for embedding, (command, link) in embedding_dict.items():
        similarity = cosine_similarity([embedding], [user_embedding])

        # If the heap is not full yet, add the current similarity
        if len(top3_heap) < 3:
            heappush(top3_heap, (similarity, link, command))
        else:
            # If the current similarity is greater than the smallest in the heap,
            # replace the smallest with the current similarity
            if similarity > top3_heap[0][0]:
                heappop(top3_heap)
                heappush(top3_heap, (similarity, link, command))
        
        elapsed_time = end_time-start_time
    
    top3_results = [(command, link, similarity) for _, command, link in sorted(top3_heap, reverse=True)]

    return top3_results,elapsed_time


def main():
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="Search for similar descriptions and get corresponding command and link.")
    parser.add_argument("user_input", help="User input description for search")
    args = parser.parse_args()
    top3, elapsed_time = search_similar_descriptions(args.user_input)

    print(top3)
    print("\n")
    if top3:
        link, command, similarity = top3[0][0], top3[0][1], top3[0][2]
        print("Command:", command)
        print("Link:", link)
        print("Similarity:", similarity[0][0])

    print("time:",elapsed_time)
    

if __name__ == "__main__":
    main()