import re

def parse_stat_block(stat_block):
    parsed_stat_block = {}

    parsed_stat_block["Name"] = extract_name(stat_block)
    parsed_stat_block.update(extract_size_alignment(stat_block))
    parsed_stat_block["Armor Class"] = extract_armor_class(stat_block)
    parsed_stat_block.update(extract_hit_points(stat_block))
    parsed_stat_block.update(extract_abilities(stat_block))
    parsed_stat_block["Senses"] = extract_senses(stat_block)
    parsed_stat_block.update(extract_challenge_rating(stat_block))
    parsed_stat_block["Actions"] = extract_actions(stat_block)

    return parsed_stat_block

def extract_name(stat_block):
    name_pattern = re.compile(r'^\s*\[?([\w\s]+)\]?\n', re.MULTILINE)
    name_match = re.search(name_pattern, stat_block)
    return name_match.group(1).strip() if name_match else None

def extract_size_alignment(stat_block):
    size_alignment_pattern = re.compile(r'^(.+), (.+)\n', re.MULTILINE)
    size_alignment_match = re.search(size_alignment_pattern, stat_block)
    if size_alignment_match:
        size, alignment = size_alignment_match.groups()
        size = size.strip()
        if 'ft.' in size:
            return {"Speed": size, "Alignment": alignment.strip()}
        else:
            return {"Size": size, "Alignment": alignment.strip()}
    return {}

def extract_armor_class(stat_block):
    armor_class_pattern = re.compile(r'Armor Class (\d+)', re.MULTILINE)
    armor_class_match = re.search(armor_class_pattern, stat_block)
    return int(armor_class_match.group(1)) if armor_class_match else None

def extract_hit_points(stat_block):
    hit_points_pattern = re.compile(r'Hit Points (\d+) \((.+)\)', re.MULTILINE)
    hit_points_match = re.search(hit_points_pattern, stat_block)
    if hit_points_match:
        return {"Hit Points": hit_points_match.group(1), "Hit Dice": hit_points_match.group(2)}
    return {}

def extract_abilities(stat_block):
    abilities_pattern = re.compile(r'(\w{3})\s(\-?\d+) \(([\+\-]?\d+)\)', re.MULTILINE)
    abilities_matches = re.findall(abilities_pattern, stat_block)
    if abilities_matches:
        return {"Abilities": {ability[0]: (int(ability[1]), int(ability[2])) for ability in abilities_matches}}
    return {}

def extract_senses(stat_block):
    senses_pattern = re.compile(r'Senses (.+)', re.MULTILINE)
    senses_match = re.search(senses_pattern, stat_block)
    return senses_match.group(1) if senses_match else None

def extract_challenge_rating(stat_block):
    challenge_rating_pattern = re.compile(r'Challenge (\d+) \((\d+) XP\)', re.MULTILINE)
    challenge_rating_match = re.search(challenge_rating_pattern, stat_block)
    if challenge_rating_match:
        return {"Challenge Rating": challenge_rating_match.group(1), "Experience Points": challenge_rating_match.group(2)}
    return {}

def extract_actions(stat_block):
    # Define the pattern to match the Actions section
    actions_pattern = re.compile(r'Actions\s*((?:.|\n)*?)(?=Legendary Actions|$)', re.MULTILINE)
    
    # Search for the Actions section in the stat block
    actions_match = re.search(actions_pattern, stat_block)
    
    # Initialize a list to store individual actions
    individual_actions = []
    
    # If the Actions section is found
    if actions_match:
        # Extract the text of the Actions section
        actions_text = actions_match.group(1)
        
        # Define the pattern to match individual actions
        individual_action_pattern = re.compile(r'^\s*([A-Za-z]+(?: [A-Za-z]+)*)\.\s*(.+?)(?=\n\s*[A-Za-z]+(?: [A-Za-z]+)*\.|\Z)', re.MULTILINE | re.DOTALL)
        
        # Search for individual actions within the Actions section
        for match in re.finditer(individual_action_pattern, actions_text):
            action_name = match.group(1).strip()
            action_details = match.group(2).strip()
            individual_actions.append({"Name": action_name, "Details": action_details})
    
    return individual_actions




# Test blocks
test_blocks = [
    """
    Goblin
    Small humanoid (goblinoid), neutral evil

        Armor Class 15 (leather armor, shield)
        Hit Points 7 (2d6)
        Speed 30 ft.

    STR
    8 (-1)
    DEX
    14 (2)
    CON
    10 (0)
    INT
    10 (0)
    WIS
    8 (-1)
    CHA
    8 (-1)

        Skills Stealth +6
        Senses darkvision 60 ft., passive Perception 9
        Languages Common, Goblin
        Challenge 1/4 (50 XP)

        Nimble Escape. The goblin can take the Disengage or Hide action as a bonus action on each of its turns.

    Actions

        Scimitar. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: (1d6+2) slashing damage.
        Shortbow. Ranged Weapon Attack: +4 to hit, reach 80/320 ft., one target. Hit: (1d6+2) piercing damage.
    """,
    """
    [Yet Another Creature]
    
    Armor Class 16 (natural armor)
    Hit Points 80 (10d10 + 30)
    Speed 30 ft., burrow 20 ft., climb 20 ft., fly 60 ft.

STR
18 (+4)
DEX
14 (+2)
CON
16 (+3)
INT
12 (+1)
WIS
10 (+0)
CHA
7 (-2)

    Skills Perception +4, Stealth +6
    Senses blindsight 60 ft., darkvision 120 ft., passive Perception 14
    Languages Common, Undercommon
    Challenge 5 (1,800 XP)

    Magic Resistance. The creature has advantage on saving throws against spells and other magical effects.
    Pack Tactics. The creature has advantage on an attack roll against a creature if at least one of the creature's allies is within 5 feet of the creature and the ally isn't incapacitated.

Actions

    Multiattack. The creature makes three attacks: one with its bite and two with its claws.
    Bite. Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: (1d10 + 4) piercing damage.
    Claw. Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: (2d6 + 4) slashing damage.
    """,
    """Ancient Brass Dragon
Gargantuan dragon, Chaotic Good

    Armor Class 20 (Natural Armor)
    Hit Points 297 (17d20+119)
    Speed 40 ft., burrow 40 ft., fly 80 ft.

STR
27 (+8)
DEX
10 (+0)
CON
25 (+7)
INT
16 (+3)
WIS
15 (+2)
CHA
19 (+4)

    Saving Throws Dex +6, Con +13, Wis +8, Cha +10
    Skills History +9, Perception +14, Persuasion +10, Stealth +6
    Damage Immunities Fire
    Senses Blindsight 60 Ft., Darkvision 120 Ft., passive Perception 24
    Languages Common, Draconic
    Challenge 20 (25,000 XP)

    Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead.

Actions

    Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.
    Bite. Melee Weapon Attack: +14 to hit, reach 15 ft., one target. Hit: (2d10 + 8) piercing damage.
    Claw. Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: (2d6 + 8) slashing damage.
    Tail. Melee Weapon Attack: +14 to hit, reach 20 ft., one target. Hit: (2d8 + 8) bludgeoning damage.
    Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 18 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.
    Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons:
    Fire Breath. The dragon exhales fire in an 90-foot line that is 10 feet wide. Each creature in that line must make a DC 21 Dexterity saving throw, taking 56 (16d6) fire damage on a failed save, or half as much damage on a successful one.
    Sleep Breath. The dragon exhales sleep gas in a 90-foot cone. Each creature in that area must succeed on a DC 21 Constitution saving throw or fall unconscious for 10 minutes. This effect ends for a creature if the creature takes damage or someone uses an action to wake it.
    Change Shape. The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the dragon's choice).
    In a new form, the dragon retains its alignment, hit points, Hit Dice, ability to speak, proficiencies, Legendary Resistance, lair actions, and Intelligence, Wisdom, and Charisma scores, as well as this action. Its statistics and capabilities are otherwise replaced by those of the new form, except any class features or legendary actions of that form.

Legendary Actions
Ancient Brass Dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature’s turn. Ancient Brass Dragon regains spent legendary actions at the start of their turn.

    Detect.The dragon makes a Wisdom (Perception) check.
    Tail Attack.The dragon makes a tail attack.
    Wing Attack (Costs 2 Actions).The dragon beats its wings. Each creature within 15 ft. of the dragon must succeed on a DC 22 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed.

""",
]

# Loop through each test block
for i, test_block in enumerate(test_blocks, start=1):
    print(f"Test Block {i}:")
    print("-" * 20)
    
    # Call the parse_stat_block function with the current test block
    parsed_result = parse_stat_block(test_block)
    
    # Print the parsed result
    print("Parsed Result:")
    print(parsed_result)
    print()
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    
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