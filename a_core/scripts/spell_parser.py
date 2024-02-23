import re

def parse_spell_description(description):
    spell_type = None
    effect = None
    
    # Define regular expressions for detecting spell types and effects
    damage_regex = re.compile(r'(?:damage|attack|hit)')
    healing_regex = re.compile(r'(?:heal|regain hit points)')
    utility_regex = re.compile(r'(?:utility|effect|condition)')
    
    # Check for spell type
    if damage_regex.search(description, re.IGNORECASE):
        spell_type = 'Damage Dealing'
    elif healing_regex.search(description, re.IGNORECASE):
        spell_type = 'Healing'
    elif utility_regex.search(description, re.IGNORECASE):
        spell_type = 'Utility'
    
    # Check for specific effects
    if 'higher level' in description.lower():
        effect = 'Casts at higher levels'
    elif 'range' in description.lower() and 'target' in description.lower():
        effect = 'Direct Target'
    elif 'range' in description.lower() and 'area' in description.lower():
        effect = 'Area of Effect'
    
    return spell_type, effect

# Test function with example spell descriptions
spell_descriptions = [
    """Fire Bolt
    Cantrip Evocation
    
        Casting Time: 1 action
        Range: 120 feet
        Target: A creature or object within range
        Components: V S
        Duration: Instantaneous
        Classes: Sorcerer, Wizard
        You hurl a mote of fire at a creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 fire damage. A flammable object hit by this spell ignites if it isn’t being worn or carried. This spell’s damage increases by 1d10 when you reach 5th level (2d10), 11th level (3d10), and 17th level (4d10).
    """,
    """Mass Healing Word
    3 Evocation
    
        Casting Time: 1 bonus action
        Range: 60 feet
        Target: Up to six creatures of your choice that you can see within range
        Components: V
        Duration: Instantaneous
        Classes: Cleric
        As you call out words of restoration, up to six creatures of your choice that you can see within range regain hit points equal to 1d4 + your spellcasting ability modifier. This spell has no effect on undead or constructs.
        At Higher Levels: When you cast this spell using a spell slot of 4th level or higher, the Healing increases by 1d4 for each slot level above 3rd.
    """,
    """Web
    2 Conjuration
    
        Casting Time: 1 action
        Range: 60 feet
        Target: A point of your choice within range
        Components: V S M (A bit of spiderweb)
        Duration: Up to 1 hour
        Classes: Sorcerer, Wizard
        You conjure a mass of thick, sticky webbing at a point of your choice within range. The webs fill a 20-foot cube from that point for the duration. The webs are difficult terrain and lightly obscure their area.
        If the webs aren’t anchored between two solid masses (such as walls or trees) or layered across a floor, wall, or ceiling, the conjured web collapses on itself, and the spell ends at the start of your next turn. Webs layered over a flat surface have a depth of 5 feet.
        Each creature that starts its turn in the webs or that enters them during its turn must make a Dexterity saving throw. On a failed save, the creature is restrained as long as it remains in the webs or until it breaks free.
        A creature restrained by the webs can use its action to make a Strength check against your spell save DC. If it succeeds, it is no longer restrained.
        The webs are flammable. Any 5-foot cube of webs exposed to fire burns away in 1 round, dealing 2d4 fire damage to any creature that starts its turn in the fire.
    """
]

for description in spell_descriptions:
    spell_type, effect = parse_spell_description(description)
    print(f"Spell Type: {spell_type}, Effect: {effect}")
