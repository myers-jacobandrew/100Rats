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

    # Initialize variables to store extracted information
    parsed_stat_block = {}

    # Extract information from the stat block using regular expressions
    name_match = re.search(name_pattern, stat_block)
    if name_match:
        parsed_stat_block["Name"] = name_match.group(1)

    size_alignment_match = re.search(size_alignment_pattern, stat_block)
    if size_alignment_match:
        parsed_stat_block["Size"], parsed_stat_block["Alignment"] = size_alignment_match.groups()

    armor_class_match = re.search(armor_class_pattern, stat_block)
    if armor_class_match:
        parsed_stat_block["Armor Class"] = int(armor_class_match.group(1))

    hit_points_match = re.search(hit_points_pattern, stat_block)
    if hit_points_match:
        parsed_stat_block["Hit Points"], parsed_stat_block["Hit Dice"] = hit_points_match.groups()

    speed_match = re.search(speed_pattern, stat_block)
    if speed_match:
        parsed_stat_block["Speed"] = speed_match.group(1)

    abilities_matches = re.findall(abilities_pattern, stat_block)
    if abilities_matches:
        parsed_stat_block["Abilities"] = {ability[0]: (int(ability[1]), int(ability[2])) for ability in abilities_matches}

    senses_match = re.search(senses_pattern, stat_block)
    if senses_match:
        parsed_stat_block["Senses"] = senses_match.group(1)

    challenge_rating_match = re.search(challenge_rating_pattern, stat_block)
    if challenge_rating_match:
        parsed_stat_block["Challenge Rating"], parsed_stat_block["Experience Points"] = challenge_rating_match.groups()

    actions_match = re.search(actions_pattern, stat_block)
    if actions_match:
        parsed_stat_block["Actions"] = actions_match.group(1)

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