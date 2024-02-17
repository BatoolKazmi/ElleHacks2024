import csv

# Define the filename of the input CSV file
input_filename = "./ElleHacks2024/csv_and_py/base_log.csv"

# Define the filename of the output CSV file
output_filename = "./ElleHacks2024/csv_and_py/filtered_tweets_cancelled.csv"

# Define an empty list to store filtered tweets
filtered_tweets = []

# Open the input CSV file
with open(input_filename, 'r', newline='', encoding='utf-8') as input_file:
    # Create a CSV reader object
    reader = csv.DictReader(input_file)
    
    # Iterate over each row in the input CSV file
    for row in reader:
        # Check if the tweet content contains the keyword "cancelled"
        if "cancelled" in row['content'].lower():
            # If it does, add the tweet content and date to the filtered_tweets list
            filtered_tweets.append((row['content'], row['date']))  # Adjusted to handle extra space

# Open the output CSV file
with open(output_filename, 'w', newline='', encoding='utf-8') as output_file:
    # Create a CSV writer object
    writer = csv.writer(output_file)
    
    # Write the header row to the output CSV file
    writer.writerow(['content', 'date'])
    
    # Write each filtered tweet to the output CSV file
    for tweet, date in filtered_tweets:
        writer.writerow([tweet, date])
