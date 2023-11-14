import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string
import csv

# Step 1: Load CSV Data
# Replace 'data.csv' with your actual CSV file name
file_path = '../dataset/AOS8/command_desc.csv'

df = pd.read_csv(file_path)
text_data = df['Description']

# Step 2: Clean and Prepare Text Data
text_data = text_data.apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)).lower())

print(text_data)
# Step 3: Generate Word Cloud
all_text = ' '.join(text_data)
wordcloud = WordCloud(width=800, height=400, max_words=200, background_color='white').generate(all_text)

# Step 4: Display the Word Cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

wordcloud.to_file("wordcloud.png")
