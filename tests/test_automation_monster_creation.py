import os
import django
from django.test import TestCase
from a_core.scripts.stat_parser import StatBlockParser

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "a_core.settings")
django.setup()

from a_posts.models import Monster

class MonsterParsingTestCase(TestCase):
    def test_stat_block_parsing(self):
        # Sample stat block
        stat_block = """
        Goblin
        Small humanoid (goblinoid), Neutral Evil

            Armor Class 15 (Leather Armor, Shield)
            Hit Points 7 (2d6)
            Speed 30 ft.

        STR
        8 (-1)
        DEX
        14 (+2)
        CON
        10 (+0)
        INT
        10 (+0)
        WIS
        8 (-1)
        CHA
        8 (-1)

            Skills Stealth +6
            Senses Darkvision 60 Ft., passive Perception 9
            Languages Common, Goblin
            Challenge 1/4 (50 XP)

            Nimble Escape. The goblin can take the Disengage or Hide action as a bonus action on each of its turns.

        Actions

            Scimitar. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: (1d6 + 2) slashing damage.
            Shortbow. Ranged Weapon Attack: +4 to hit, reach 80/320 ft., one target. Hit: (1d6 + 2) piercing damage.
        """

        # Create an instance of the parser
        parser = StatBlockParser()

        # Parse the stat block
        parsed_data = parser.parse_stat_block(stat_block)

        # Verify that the parsing was successful
        self.assertEqual(parsed_data['Name'], 'Goblin')
        self.assertEqual(parsed_data['Size'], 'Small humanoid (goblinoid)')
        self.assertEqual(parsed_data['Alignment'], 'Neutral Evil')
        self.assertEqual(parsed_data['Armor Class'], 15)
        self.assertEqual(parsed_data['Hit Points'], '7')
        self.assertEqual(parsed_data['Hit Dice'], '2d6')
        self.assertEqual(parsed_data['Speed'], '30 ft.')
        # Add more assertions...

        # Create a Monster instance with the parsed data
        monster = Monster(**parsed_data)
        monster.save()

        # Verify that the Monster was saved successfully
        saved_monster = Monster.objects.get(id=monster.id)
        self.assertEqual(saved_monster.name, 'Goblin')
        # Add more assertions....


if __name__ == "__main__":
    import sys
    from django.core.management import execute_from_command_line

    # Setup Django environment and execute tests
    execute_from_command_line(sys.argv + ['test', 'a_posts.tests.MonsterParsingTestCase'])
