import os
import re

# Function to clean and process the text for each race
def clean_race_text(text):
    # Remove extra whitespace and newlines
    cleaned_text = text.strip()

    # Remove contents in square brackets
    cleaned_text = re.sub(r'\[.*?\]', '', cleaned_text)

    # Remove contents in parentheses
    cleaned_text = re.sub(r'\(.*?\)', '', cleaned_text)

    # Remove multiple spaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    return cleaned_text

# Function to process each race file
def process_race_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        race_text = file.read()

    cleaned_race_text = clean_race_text(race_text)

    return cleaned_race_text

# Directory where race files are stored (relative to the script's directory)
race_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'race_data'))

# Process each race file
for filename in os.listdir(race_directory):
    if filename.endswith('.txt'):
        race_filename = os.path.join(race_directory, filename)
        cleaned_race_text = process_race_file(race_filename)

        # Write cleaned text back to the file
        with open(race_filename, 'w', encoding='utf-8') as file:
            file.write(cleaned_race_text)

        print(f"Processed and cleaned {filename}")

print("All race files processed and cleaned.")
