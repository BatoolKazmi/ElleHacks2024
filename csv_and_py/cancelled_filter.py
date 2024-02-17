import csv
import os
from openai import OpenAI

cwd = os.path.dirname(os.path.abspath(__file__))
print(cwd)

client = OpenAI(api_key = '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')
prompt = "Your prompt here. For example, 'Once upon a time...'"

input_filename = "base_log.csv"

output_filename = "filtered_tweets_cancelled.csv"

# Construct the absolute file paths
input_filepath = os.path.join(cwd, input_filename)
output_filepath = os.path.join(cwd, output_filename)

iprompt = ["I will give you content. You must strictly use this format to give a generated response"
           "I need to use the content you give back to me in a CSV file."
           "This information is about bus cancellation."
           "I want you to carefully find out the main information that is conveyed through this content."
           "Your format must be: time mentioned in content (in 24 hour format), 'bus number __ has been cancelled',"
           "Here is your content: "]

# Define an empty list to store filtered tweets
filtered_tweets = []

with open(input_filepath, 'r', newline='', encoding='utf-8') as input_file:
    # Create a CSV reader object
    reader = csv.DictReader(input_file)
    
    # Iterate over each row in the input CSV file
    for row in reader:
        # Check if the tweet content contains the keyword "cancelled"
        if "cancelled" in row['content'].lower():
            prompt = iprompt.append(row['content'])
            print(iprompt)
            print(prompt)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100
            )
            generated_text = response.choices[0].message.content
            print(generated_text)
            # If it does, add the tweet content and date to the filtered_tweets list
            filtered_tweets.append((row['content'], row['date'], generated_text))
print(filtered_tweets)


with open(output_filepath, 'w', newline='', encoding='utf-8') as output_file:
    # Create a CSV writer object
    writer = csv.writer(output_file)
    
    # Write the header row
    writer.writerow(['content', 'date', 'generated_response'])
    
    # Write each filtered tweet to the output CSV file
    for tweet, date, response in filtered_tweets:
        writer.writerow([tweet, date, response])
