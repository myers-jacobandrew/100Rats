import re


class StatBlockParser:
    def __init__(self):
        pass

    def parse_stat_block(self, stat_block):
        parsed_stat_block = {}
        parsed_stat_block["Name"] = self.extract_name(stat_block)
        parsed_stat_block.update(self.extract_size_alignment(stat_block))
        parsed_stat_block["Armor Class"] = self.extract_armor_class(stat_block)
        parsed_stat_block.update(self.extract_hit_points(stat_block))
        parsed_stat_block["Speed"] = self.extract_speed(stat_block)  
        parsed_stat_block.update(self.extract_abilities(stat_block))
        parsed_stat_block["Senses"] = self.extract_senses(stat_block)
        parsed_stat_block.update(self.extract_challenge_rating(stat_block))
        parsed_stat_block.update(self.extract_special_abilities(stat_block))  
        actions, legendary_actions, legendary_actions_count = self.extract_actions(stat_block)
        parsed_stat_block["Actions"] = actions
        parsed_stat_block["Legendary Actions"] = legendary_actions if legendary_actions is not None else []
        
        return parsed_stat_block

    def extract_name(self, stat_block):
        name_pattern = re.compile(r'^\s*\[?([\w\s]+)\]?\n', re.MULTILINE)
        name_match = re.search(name_pattern, stat_block)
        return name_match.group(1).strip() if name_match else None

    def extract_size_alignment(self, stat_block):
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

    def extract_armor_class(self, stat_block):
        armor_class_pattern = re.compile(r'Armor Class (\d+)', re.MULTILINE)
        armor_class_match = re.search(armor_class_pattern, stat_block)
        return int(armor_class_match.group(1)) if armor_class_match else None

    def extract_hit_points(self, stat_block):
        hit_points_pattern = re.compile(r'Hit Points (\d+) \((.+)\)', re.MULTILINE)
        hit_points_match = re.search(hit_points_pattern, stat_block)
        if hit_points_match:
            return {"Hit Points": hit_points_match.group(1), "Hit Dice": hit_points_match.group(2)}
        return {}
    
    def extract_speed(self, stat_block):
        speed_pattern = re.compile(r'Speed (.+?)\n', re.MULTILINE)
        speed_match = re.search(speed_pattern, stat_block)
        return speed_match.group(1) if speed_match else None

    def extract_abilities(self, stat_block):
        abilities_pattern = re.compile(r'(\w{3})\s(\-?\d+) \(([\+\-]?\d+)\)', re.MULTILINE)
        abilities_matches = re.findall(abilities_pattern, stat_block)
        if abilities_matches:
            return {"Abilities": {ability[0]: (int(ability[1]), int(ability[2])) for ability in abilities_matches}}
        return {}

    def extract_senses(self, stat_block):
        senses_pattern = re.compile(r'Senses (.+)', re.MULTILINE)
        senses_match = re.search(senses_pattern, stat_block)
        return senses_match.group(1) if senses_match else None

    def extract_challenge_rating(self, stat_block):
        challenge_rating_pattern = re.compile(r'Challenge (\d+) \((\d+) XP\)', re.MULTILINE)
        challenge_rating_match = re.search(challenge_rating_pattern, stat_block)
        if challenge_rating_match:
            return {"Challenge Rating": challenge_rating_match.group(1), "Experience Points": challenge_rating_match.group(2)}
        return {}

    def extract_special_abilities(self, stat_block):
        special_abilities = {}
        special_abilities_pattern = re.compile(r' XP\)\n(.*?)(?=\n\nActions\n|\Z)', re.DOTALL)
        special_abilities_match = re.search(special_abilities_pattern, stat_block)
        if special_abilities_match:
#            print("Special abilities pattern matched.")   
            # Extract the matched text
            special_abilities_text = special_abilities_match.group(1)
#            print("Special Abilitie Text:"+special_abilities_text)
            # Clean the extracted text
            cleaned_special_abilities = special_abilities_text.strip()
#            print("Special Abilitie Text Cleaned:"+cleaned_special_abilities)
        return {"Special Abilities": cleaned_special_abilities}

    
    def extract_actions(self, stat_block):
        actions = []
        legendary_actions = []
        legendary_action_count = 0

        # Extract the actions section
        actions_section = re.findall(r"Actions\n(?:\s+)(.*?)(?:Legendary Actions|\Z)", stat_block, re.DOTALL)
        if actions_section:
            action_text = actions_section[0].strip()  # Extracting actions text
            action_matches = re.findall(r"^\s*([A-Za-z\s]+)\. (.*?)(?=\n\s*[A-Za-z\s]+\. |\n\n|\Z)", action_text, re.DOTALL | re.MULTILINE)
            for action_match in action_matches:
                actions.append({
                    "Action Name": action_match[0].strip(),
                    "Action Description": action_match[1].strip()
                })

        # Extract legendary actions if they exist
        if "Legendary Actions" in stat_block:
            legendary_text = stat_block.split("Legendary Actions")[1].strip()  # Extract legendary actions text
            legendary_actions, legendary_action_count = self.extract_legendary_actions(legendary_text)  # Extract legendary actions
#            print("legendary_text:"+legendary_text)
            
        # Ensure that actions and legendary_actions are always lists
        return actions, legendary_actions, legendary_action_count

    def extract_legendary_actions(self, text):
        legendary_actions = []
        legendary_action_count = 0

        # Extract the count of legendary actions
        action_count_match = re.search(r"(\d+) legendary actions", text)
        if action_count_match:
            legendary_action_count = int(action_count_match.group(1))

        # Find the index where legendary actions start using regex
        action_start_match = re.search(r"\n\n", text)
        if action_start_match:
            start_index = action_start_match.end()
            legendary_actions_text = text[start_index:].strip()

        # Remove leading/trailing whitespace
        legendary_actions_text = legendary_actions_text.strip()

        # Split legendary actions by newline followed by an indented line,
        # capturing cost information within parentheses (optional)
        action_blocks = re.findall(
            r"^([\w\s]+)\s*(?:\(([^)]+)\)\.\s)?(.*?)(?:\n|$)",
            legendary_actions_text,
            re.DOTALL | re.MULTILINE,
        )

        # Append all legendary actions
        for action_name, cost, action_description in action_blocks:
            # Combine action name and cost if present, otherwise use only action name
            if cost:
                action_name = f"{action_name.strip()} (Cost {cost.strip()} Actions)"
            else:
                action_name = action_name.strip()

            # Split the description at the newline character if present
            if '\n' in action_description:
                action_description, additional_description = action_description.split('\n', 1)
                legendary_actions.append({"Legendary Action": action_name, "Legendary Action Description": action_description.strip()})
                legendary_actions.append({"Legendary Action": action_name, "Legendary Action Description": additional_description.strip()})
            else:
                legendary_actions.append({"Legendary Action": action_name, "Legendary Action Description": action_description.strip()})

        return legendary_actions, legendary_action_count









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


# Instantiate the StatBlockParser
parser = StatBlockParser()

# Loop through each test block
for i, test_block in enumerate(test_blocks, start=1):
    print(f"Test Block {i}:")
    print("-" * 20)
    
    # Call the parse_stat_block method of the parser object with the current test block
    parsed_result = parser.parse_stat_block(test_block)
    print()
    print("-" * 20)
    # Print the parsed result
    print("Parsed Result:")
    print(parsed_result)
    print()
