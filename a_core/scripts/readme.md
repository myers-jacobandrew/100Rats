# spell_parser.py

## Overview
This script parses descriptions of spells and extracts their types and effects. It utilizes regular expressions to identify spell types (such as damage-dealing, healing, or utility) and specific effects (such as casting at higher levels or basic targeting options).


Example Usage

    The script currently supports basic spell types and effects, specifically direct damaging spells, AoE spells, Healing spells, basic utility spells. Needs more love to support additional types or effects.

## Example Output Format
Here's an example of the expected format:

`Spell Type: <Type>, Effect: <Effect>`


# stat_parser.py
Overview

This script parses stat blocks of creatures in the Dungeons & Dragons 5th Edition (5e) system. It extracts relevant information such as name, size, type, stats, abilities, actions, and legendary actions from a copy and pasted stat block. Test cases with example enemy stat blocks are provided at the end of the script.
Example Stat Block Format

Here's an example of the expected input format:

```
Creature Name
Size Type, Alignment

Armor Class 15
Hit Points 50 (10d8 + 10)
Speed 30 ft., swim 60 ft.

STR 18 (+4)
DEX 14 (+2)
CON 14 (+2)
INT 10 (+0)
WIS 13 (+1)
CHA 8 (-1)

Saving Throws Str +6, Con +4
Skills Athletics +6, Perception +3
Damage Resistances bludgeoning, piercing, and slashing from nonmagical attacks
Senses darkvision 60 ft., passive Perception 13
Languages Common, Elvish
Challenge 3 (700 XP)

Actions

Multiattack. The creature makes two melee attacks.
Greataxe. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (1d12 + 4) slashing damage.
Javelin. Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage.

Legendary Actions
The creature can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature’s turn. The creature regains spent legendary actions at the start of its turn.

Detect. The creature makes a Wisdom (Perception) check.
Tail Attack. The creature makes a tail attack.
Wing Attack (Costs 2 Actions). The creature beats its wings. Each creature within 15 ft. of the creature must succeed on a DC 15 Dexterity saving throw or take 15 (2d6 + 2) bludgeoning damage and be knocked prone. The creature can then fly up to half its flying speed.
```

## Usage

To use the Stat Block Parser, copy and paste the creature's stat block into the provided function. Then, execute the script to obtain a dictionary containing the parsed information.

# Instantiate the StatBlockParser
parser = StatBlockParser()

# Parse a stat block
parsed_result = parser.parse_stat_block(stat_block)

# Print the parsed result
print(parsed_result)

## License
This script is provided under the MIT License. See the LICENSE file for more information.
