import csv
import os
import openai

cwd = os.path.dirname(os.path.abspath(__file__))
print(cwd)
openai.api_key = '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'
prompt = "Your prompt here. For example, 'Once upon a time...'"

# Define the filename of the input CSV file
input_filename = "base_log.csv"

# Define the filename of the output CSV file
output_filename = "filtered_tweets_cancelled.csv"

# Construct the absolute file paths
input_filepath = os.path.join(cwd, input_filename)
output_filepath = os.path.join(cwd, output_filename)


# Define an empty list to store filtered tweets
filtered_tweets = []

# Open the input CSV file
with open(input_filepath, 'r', newline='', encoding='utf-8') as input_file:
    # Create a CSV reader object
    reader = csv.DictReader(input_file)
    
    # Iterate over each row in the input CSV file
    for row in reader:
        # Check if the tweet content contains the keyword "cancelled"
        if "cancelled" in row['content'].lower():
            # If it does, add the tweet content and date to the filtered_tweets list
            filtered_tweets.append((row['content'], row['date']))  # Adjusted to handle extra space


# Open the output CSV file
with open(output_filepath, 'w', newline='', encoding='utf-8') as output_file:
    # Create a CSV writer object
    writer = csv.writer(output_file)
    
    # Write the header row to the output CSV file
    writer.writerow(['content', 'date'])
    
    # Write each filtered tweet to the output CSV file
    for tweet, date in filtered_tweets:
        writer.writerow([tweet, date])
