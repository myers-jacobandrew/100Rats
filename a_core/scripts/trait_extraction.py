import os
import re

# Directory where race files are stored (relative to the script's directory)
race_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'race_data'))

# Function to extract racial traits from text
def racial_traits(text):
    traits = {}
    pattern = r'Ability Score Increase\..*?Age\..*?Size\..*?Speed\..*?Languages\..*?'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        traits_text = match.group(0)
        lines = traits_text.split('\n')
        for line in lines:
            if '.' in line:
                trait_name, trait_details = line.split('.', 1)
                trait_name = trait_name.strip()
                trait_details = trait_details.strip()
                traits[trait_name] = trait_details
    return traits

# Function to extract battle traits from text
def battle_traits(text):
    # Define patterns for detecting specific traits
    patterns = {
        'Ability Score Increase': r'Ability Score Increase\..*',
        'Speed': r'Speed\..*',
        'Resistance': r'(resistance to [a-zA-Z\s]+ damage)',
        'Proficiency': r'(gain proficiency in [a-zA-Z\s]+ skill|tool)',
        'Special Ability': r'(You have [a-zA-Z\s]+|You can cast [a-zA-Z\s]+)',
        'Spellcasting': r'(You can cast [a-zA-Z\s]+)',
    }
    traits = {}
    for trait, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            traits[trait] = match.group(0)
    return traits

# Function to parse traits data from files
def parse_traits_data():
    traits_data = {}
    for filename in os.listdir(race_directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(race_directory, filename)
            with open(file_path, 'r') as file:
                race_text = file.read()
            # Extract racial traits and battle traits
            race_traits = racial_traits(race_text)
            battle_traits = battle_traits(race_text)
            # Store the traits data
            traits_data[filename] = {'racial_traits': race_traits, 'battle_traits': battle_traits}
    return traits_data

# Main function
def main():
    # Parse traits data from files
    traits_data = parse_traits_data()

    # Subrace selection
    print("Available subraces:")
    for subrace, data in traits_data.items():
        print(subrace)
    selected_subrace = input("Select your subrace: ")

    # Display selected subrace traits
    if selected_subrace in traits_data:
        print("Racial Traits:")
        for trait, details in traits_data[selected_subrace]['racial_traits'].items():
            print(f"{trait}: {details}")
        print("\nBattle Traits:")
        for trait, details in traits_data[selected_subrace]['battle_traits'].items():
            print(f"{trait}: {details}")
    else:
        print("Invalid subrace selection.")

if __name__ == "__main__":
    main()
