import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')
nltk.download('stopwords')

custom_stop_words = ["command", "displays", "purpose"]
stop_words = set(stopwords.words('english') + custom_stop_words)

def preprocess_text(description):
    description = description.lower()

    tokens = word_tokenize(description)

    tokens = [token for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stop_words]

    # Joining tokens back into a string
    preprocessed_description = ' '.join(tokens)

    return preprocessed_description

# Read the existing CSV file
file_path = "embeddings_data.csv"
df = pd.read_csv(file_path)

# Add a new column with preprocessed descriptions
df['Preprocessed_Description'] = df['Description'].apply(preprocess_text)
output_file_path = "updated_embeddings_data.csv"
# Save the updated DataFrame to the same CSV file
df.to_csv(output_file_path, index=False)

# Print the DataFrame with the new column
print(df)
