import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Create the directory if it doesn't exist
os.makedirs('race_data', exist_ok=True)

urls = [
    "https://dnd-5e.fandom.com/wiki/Aarakocra_(Race)",
    "https://dnd-5e.fandom.com/wiki/Aasimar",
    "https://dnd-5e.fandom.com/wiki/Aetherborn",
    "https://dnd-5e.fandom.com/wiki/Astral_Elf",
    "https://dnd-5e.fandom.com/wiki/Autognome_(Race)",
    "https://dnd-5e.fandom.com/wiki/Aven",
    "https://dnd-5e.fandom.com/wiki/Bugbear_(Race)",
    "https://dnd-5e.fandom.com/wiki/Centaur",
    "https://dnd-5e.fandom.com/wiki/Centaur_(Race)",
    "https://dnd-5e.fandom.com/wiki/Changeling",
    "https://dnd-5e.fandom.com/wiki/Changeling_(Race)",
    "https://dnd-5e.fandom.com/wiki/Changeling_(Race)",
    "https://dnd-5e.fandom.com/wiki/Deep_Gnome_(Race)",
    "https://dnd-5e.fandom.com/wiki/Dhampir",
    "https://dnd-5e.fandom.com/wiki/Dragonborn",
    "https://dnd-5e.fandom.com/wiki/Duergar_(Race)",
    "https://dnd-5e.fandom.com/wiki/Dwarf",
    "https://dnd-5e.fandom.com/wiki/Eladrin",
    "https://dnd-5e.fandom.com/wiki/Elf",
    "https://dnd-5e.fandom.com/wiki/Elf/Unearthed_Arcana",
    "https://dnd-5e.fandom.com/wiki/Fairy",
    "https://dnd-5e.fandom.com/wiki/Firbolg",
    "https://dnd-5e.fandom.com/wiki/Genasi",
    "https://dnd-5e.fandom.com/wiki/Giff_(Race)",
    "https://dnd-5e.fandom.com/wiki/Gith",
    "https://dnd-5e.fandom.com/wiki/Githyanki",
    "https://dnd-5e.fandom.com/wiki/Githzerai",
    "https://dnd-5e.fandom.com/wiki/Glitchling",
    "https://dnd-5e.fandom.com/wiki/Gnome",
    "https://dnd-5e.fandom.com/wiki/Goblin_(Race)",
    "https://dnd-5e.fandom.com/wiki/Goliath",
    "https://dnd-5e.fandom.com/wiki/Grung",
    "https://dnd-5e.fandom.com/wiki/Grung_(Race)",
    "https://dnd-5e.fandom.com/wiki/Hadozee",
    "https://dnd-5e.fandom.com/wiki/Half-elf",
    "https://dnd-5e.fandom.com/wiki/Half-orc",
    "https://dnd-5e.fandom.com/wiki/Halfling",
    "https://dnd-5e.fandom.com/wiki/Harengon",
    "https://dnd-5e.fandom.com/wiki/Hexblood",
    "https://dnd-5e.fandom.com/wiki/Hobgoblin",
    "https://dnd-5e.fandom.com/wiki/Hobgoblin_(Race)",
    "https://dnd-5e.fandom.com/wiki/Hollow_One",
    "https://dnd-5e.fandom.com/wiki/Human",
    "https://dnd-5e.fandom.com/wiki/Kalashtar",
    "https://dnd-5e.fandom.com/wiki/Kalashtar_(Race)",
    "https://dnd-5e.fandom.com/wiki/Kender",
    "https://dnd-5e.fandom.com/wiki/Kenku",
    "https://dnd-5e.fandom.com/wiki/Kenku_(Race)",
    "https://dnd-5e.fandom.com/wiki/Khenra",
    "https://dnd-5e.fandom.com/wiki/Kobold",
    "https://dnd-5e.fandom.com/wiki/Kobold_(Race)",
    "https://dnd-5e.fandom.com/wiki/Kor",
    "https://dnd-5e.fandom.com/wiki/Leonin",
    "https://dnd-5e.fandom.com/wiki/Lizardfolk",
    "https://dnd-5e.fandom.com/wiki/Lizardfolk_(Race)",
    "https://dnd-5e.fandom.com/wiki/Locathah",
    "https://dnd-5e.fandom.com/wiki/Loxodon",
    "https://dnd-5e.fandom.com/wiki/Merfolk",
    "https://dnd-5e.fandom.com/wiki/Merfolk_(Race)",
    "https://dnd-5e.fandom.com/wiki/Minotaur",
    "https://dnd-5e.fandom.com/wiki/Minotaur_(Race)",
    "https://dnd-5e.fandom.com/wiki/Naga",
    "https://dnd-5e.fandom.com/wiki/Orc_(Race)",
    "https://dnd-5e.fandom.com/wiki/Owlin",
    "https://dnd-5e.fandom.com/wiki/Plasmoid",
    "https://dnd-5e.fandom.com/wiki/Reborn",
    "https://dnd-5e.fandom.com/wiki/Revenant",
    "https://dnd-5e.fandom.com/wiki/Revenant_(Race)",
    "https://dnd-5e.fandom.com/wiki/Satyr_(Race)",
    "https://dnd-5e.fandom.com/wiki/Sea_Elf",
    "https://dnd-5e.fandom.com/wiki/Shadar-kai",
    "https://dnd-5e.fandom.com/wiki/Shifter",
    "https://dnd-5e.fandom.com/wiki/Shifter_(Race)",
    "https://dnd-5e.fandom.com/wiki/Simic_Hybrid",
    "https://dnd-5e.fandom.com/wiki/Siren",
    "https://dnd-5e.fandom.com/wiki/Siren_(Race)",
    "https://dnd-5e.fandom.com/wiki/Tabaxi",
    "https://dnd-5e.fandom.com/wiki/Thri-kreen_(Race)",
    "https://dnd-5e.fandom.com/wiki/Tiefling",
    "https://dnd-5e.fandom.com/wiki/Tortle",
    "https://dnd-5e.fandom.com/wiki/Tortle_(Race)",
    "https://dnd-5e.fandom.com/wiki/Triton",
    "https://dnd-5e.fandom.com/wiki/Vampire_(Race)",
    "https://dnd-5e.fandom.com/wiki/Vedalken",
    "https://dnd-5e.fandom.com/wiki/Verdan",
    "https://dnd-5e.fandom.com/wiki/Viashino",
    "https://dnd-5e.fandom.com/wiki/Warforged",
    "https://dnd-5e.fandom.com/wiki/Yuan-ti",
    "https://dnd-5e.fandom.com/wiki/Yuan-ti_Pureblood",
]


for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    page_main = soup.select_one('.page__main')

    if page_main:
        content = page_main.text.strip()
        
        # Extract race name from the URL
        race_name = urlparse(url).path.split('/')[-1]
        race_name = race_name.replace('_', ' ')  # Replace underscores with spaces
        race_name = race_name.split('(')[0].strip()  # Remove any parentheses content

        filename = f"race_data/{race_name}.txt"

        # Open the file in write mode
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"Content from {url} has been saved to {filename}")
    else:
        print(f"Failed to find content on page {url}")