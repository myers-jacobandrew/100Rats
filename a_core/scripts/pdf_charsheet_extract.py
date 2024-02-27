import pdfplumber
import re

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def process_pdf_data(pdf_text):
    # Extract and process the relevant data from the PDF text
    # For example:
    name = extract_name(pdf_text)
    race = extract_race(pdf_text)
    class_name = extract_class(pdf_text)
    level = extract_level(pdf_text)
    # Extract other fields as needed
    
    # Return a dictionary with the extracted data
    return {
        'name': name,
        'race': race,
        'class_name': class_name,
        'level': level,
        # Include other extracted fields
    }

def extract_name(text):
    name_pattern = re.compile(r'Name:\s*(.*)', re.IGNORECASE)
    match = name_pattern.search(text)
    if match:
        return match.group(1).strip()
    return None

def extract_race(text):
    race_pattern = re.compile(r'Race:\s*(.*)', re.IGNORECASE)
    match = race_pattern.search(text)
    if match:
        return match.group(1).strip()
    return None

def extract_class(text):
    class_pattern = re.compile(r'Class:\s*(.*)', re.IGNORECASE)
    match = class_pattern.search(text)
    if match:
        return match.group(1).strip()
    return None

def extract_level(text):
    level_pattern = re.compile(r'Level:\s*(.*)', re.IGNORECASE)
    match = level_pattern.search(text)
    if match:
        return match.group(1).strip()
    return None


# Example usage:
pdf_file_path = "/path/to/character_sheet.pdf"
pdf_text = extract_text_from_pdf(pdf_file_path)
character_data = process_pdf_data(pdf_text)
print(character_data)
