import re

def parse_stat_block(stat_block):
    # Define regular expressions to match different parts of the stat block
    name_pattern = re.compile(r'^([\w\s]+)\n', re.MULTILINE)
    size_alignment_pattern = re.compile(r'^(.+), (.+)\n', re.MULTILINE)
    armor_class_pattern = re.compile(r'Armor Class (\d+)', re.MULTILINE)
    hit_points_pattern = re.compile(r'Hit Points (\d+) \((.+)\)', re.MULTILINE)
    speed_pattern = re.compile(r'Speed (\d+ ft\.)', re.MULTILINE)
    abilities_pattern = re.compile(r'(\w{3})\s(\-?\d+) \(([\+\-]?\d+)\)', re.MULTILINE)
    senses_pattern = re.compile(r'Senses (.+)', re.MULTILINE)
    challenge_rating_pattern = re.compile(r'Challenge (\d+) \((\d+) XP\)', re.MULTILINE)
    actions_pattern = re.compile(r'Actions\n\n([\w\s\.,\(\)\:\-\+]+)', re.MULTILINE)

    # Extract information from the stat block using regular expressions
    name = re.search(name_pattern, stat_block).group(1)
    size, alignment = re.search(size_alignment_pattern, stat_block).groups()
    armor_class = int(re.search(armor_class_pattern, stat_block).group(1))
    hit_points, hit_dice = re.search(hit_points_pattern, stat_block).groups()
    speed = re.search(speed_pattern, stat_block).group(1)
    abilities = dict(re.findall(abilities_pattern, stat_block))
    senses = re.search(senses_pattern, stat_block).group(1)
    challenge_rating, xp = re.search(challenge_rating_pattern, stat_block).groups()
    actions = re.search(actions_pattern, stat_block).group(1)

    # Format the extracted information into a dictionary
    parsed_stat_block = {
        "Name": name,
        "Size": size,
        "Alignment": alignment,
        "Armor Class": armor_class,
        "Hit Points": hit_points,
        "Hit Dice": hit_dice,
        "Speed": speed,
        "Abilities": abilities,
        "Senses": senses,
        "Challenge Rating": challenge_rating,
        "Experience Points": xp,
        "Actions": actions
    }

    return parsed_stat_block
'''
# Example stat block
stat_block = """
Rat
Tiny beast, Unaligned

    Armor Class 10
    Hit Points 1 (1d4-1)
    Speed 20 ft.

STR
2 (-4)
DEX
11 (+0)
CON
9 (-1)
INT
2 (-4)
WIS
10 (+0)
CHA
4 (-3)

    Senses Darkvision 30 Ft., passive Perception 10
    Challenge 0 (10 XP)

    Keen Smell. The rat has advantage on Wisdom (Perception) checks that rely on smell.

Actions

    Bite. Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: (1d1) piercing damage.
"""

# Parse the stat block
parsed_stat_block = parse_stat_block(stat_block)

# Print the parsed information
for key, value in parsed_stat_block.items():
    print(f"{key}: {value}")
'''