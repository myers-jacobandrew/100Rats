from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
  # Import the User model
import uuid



class Monster(models.Model):
    INPUT_METHOD_CHOICES = [
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
    ]

    # Common fields
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=20, null=True, blank=True)
    creature_type = models.CharField(max_length=20, null=True, blank=True)
    alignment = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    input_method = models.CharField(max_length=20, choices=INPUT_METHOD_CHOICES, default='manual')
    
    # Stats
    armor_class = models.IntegerField(null=True, blank=True)
    hit_points = models.PositiveIntegerField(null=True, blank=True)
    
    speed = models.CharField(max_length=50, null=True, blank=True)
    
    # Speed fields
    land_speed = models.IntegerField(null=True, blank=True)
    burrow_speed = models.IntegerField(null=True, blank=True)
    fly_speed = models.IntegerField(null=True, blank=True)
    swim_speed = models.IntegerField(null=True, blank=True)
    
    # Abilities
    strength = models.IntegerField(null=True, blank=True)
    dexterity = models.IntegerField(null=True, blank=True)
    constitution = models.IntegerField(null=True, blank=True)
    intelligence = models.IntegerField(null=True, blank=True)
    wisdom = models.IntegerField(null=True, blank=True)
    charisma = models.IntegerField(null=True, blank=True)
    
    # Saving Throws
    saving_throws = models.TextField(null=True, blank=True)
    
    # Skills
    skills = models.TextField(null=True, blank=True)
    
    # Damage Resistances and Immunities
    damage_resistances = models.TextField(null=True, blank=True)
    damage_immunities = models.TextField(null=True, blank=True)
    condition_immunities = models.TextField(null=True, blank=True)
    
    # Senses
    senses = models.TextField(null=True, blank=True)
    
    # Languages
    languages = models.TextField(null=True, blank=True)
    
    # Challenge and XP
    challenge_rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    experience_points = models.IntegerField(null=True, blank=True)
    
    # Special, Legendary, and Lair Actions
    special_abilities = models.TextField(null=True, blank=True)
    special_abilities_count = models.IntegerField(null=True, blank=True)
    
    # Spells
    # To-do
        
    # Actions
    actions = models.TextField(null=True, blank=True)
    
    # Extras
    raw_stat_block = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


class Spell(models.Model):
    INPUT_METHOD_CHOICES = [
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
    ]

    SPELL_TYPES = [
        ('DD', 'Damage Dealing'),
        ('HL', 'Healing'),
        ('UT', 'Utility'),
        ('OT', 'Other'),
    ]
    
    MAGIC_SCHOOL_CHOICES = [
        ('abjuration', 'Abjuration'),
        ('conjuration', 'Conjuration'),
        ('divination', 'Divination'),
        ('enchantment', 'Enchantment'),
        ('evocation', 'Evocation'),
        ('illusion', 'Illusion'),
        ('necromancy', 'Necromancy'),
        ('transmutation', 'Transmutation'),
    ]
            
    # Common
    spell_name = models.CharField(max_length=100)
    spell_type = models.CharField(max_length=2, choices=SPELL_TYPES)
    input_method = models.CharField(max_length=20, choices=INPUT_METHOD_CHOICES, default='manual')
    created_at = models.DateTimeField(default=timezone.now)

    school_of_magic = models.CharField(max_length=24,choices=MAGIC_SCHOOL_CHOICES, default='')
    description = models.TextField()
    class_requirement = models.TextField(blank=True, null=True)
    effect = models.CharField(max_length=100, blank=True, null=True)
    cast_at_higher_levels = models.BooleanField(default=False)
    
    # Additional spell attributes
    casting_time = models.CharField(max_length=50, blank=True, null=True)
    spell_range = models.CharField(max_length=50, blank=True, null=True)
    spell_target = models.CharField(max_length=100, blank=True, null=True)
    spell_components = models.CharField(max_length=50, blank=True, null=True)
    spell_duration = models.CharField(max_length=50, blank=True, null=True)
    spell_classes = models.CharField(max_length=200, blank=True, null=True)
    spell_effect_description = models.TextField(blank=True, null=True)
    spell_damage_description = models.TextField(blank=True, null=True)
    spell_scaling_description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.spell_name


class CharacterClass(models.Model):
    CLASS_CHOICES = [
        ('artificer', 'Artificer'),
        ('barbarian', 'Barbarian'),
        ('bard', 'Bard'),
        ('bloodhunter','Blood Hunter'),
        ('cleric', 'Cleric'),
        ('druid', 'Druid'),
        ('fighter', 'Fighter'),
        ('monk', 'Monk'),
        ('paladin', 'Paladin'),
        ('ranger', 'Ranger'),
        ('rogue', 'Rogue'),
        ('sorcerer', 'Sorcerer'),
        ('warlock', 'Warlock'),
        ('wizard', 'Wizard'),
        # Add other classes as needed
    ]

    class_name = models.CharField(max_length=50, choices=CLASS_CHOICES)
    level = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.class_name} - Level {self.level}"


class PlayerCharacter(models.Model):
    INPUT_METHOD_CHOICES = [
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
    ]
    
    RACE_CHOICES = [
        ('human', 'Human'),
        ('elf', 'Elf'),
        ('dwarf', 'Dwarf'),
        ('halfling', 'Halfling'),
        ('aarakocra', 'Aarakocra'),
        ('aasimar', 'Aasimar'),
        ('aetherborn', 'Aetherborn'),
        ('astral_elf', 'Astral Elf'),
        ('autognome', 'Autognome'),
        ('bugbear', 'Bugbear'),
        ('centaur', 'Centaur'),
        ('changeling', 'Changeling'),
        ('deep_gnome', 'Deep Gnome'),
        ('dhampir', 'Dhampir'),
        ('dragonborn', 'Dragonborn'),
        ('duergar', 'Duergar'),
        ('eladrin', 'Eladrin'),
        ('elf_ua', 'Elf/Unearthed Arcana'),
        ('fairy', 'Fairy'),
        ('firbolg', 'Firbolg'),
        ('genasi', 'Genasi'),
        ('giff', 'Giff'),
        ('gith', 'Gith'),
        ('githyanki', 'Githyanki'),
        ('githzerai', 'Githzerai'),
        ('glitchling', 'Glitchling'),
        ('gnome', 'Gnome'),
        ('goblin', 'Goblin'),
        ('goliath', 'Goliath'),
        ('grung', 'Grung'),
        ('hadozee', 'Hadozee'),
        ('half_elf', 'Half-elf'),
        ('half_orc', 'Half-orc'),
        ('harengon', 'Harengon'),
        ('hexblood', 'Hexblood'),
        ('hobgoblin', 'Hobgoblin'),
        ('hollow_one', 'Hollow One'),
        ('kalashtar', 'Kalashtar'),
        ('kender', 'Kender'),
        ('kenku', 'Kenku'),
        ('khenra', 'Khenra'),
        ('kobold', 'Kobold'),
        ('kor', 'Kor'),
        ('leonin', 'Leonin'),
        ('lizardfolk', 'Lizardfolk'),
        ('locathah', 'Locathah'),
        ('loxodon', 'Loxodon'),
        ('merfolk', 'Merfolk'),
        ('minotaur', 'Minotaur'),
        ('naga', 'Naga'),
        ('orc', 'Orc'),
        ('owlin', 'Owlin'),
        ('plasmoid', 'Plasmoid'),
        ('reborn', 'Reborn'),
        ('revenant', 'Revenant'),
        ('satyr', 'Satyr'),
        ('sea_elf', 'Sea Elf'),
        ('shadar_kai', 'Shadar-kai'),
        ('shifter', 'Shifter'),
        ('simic_hybrid', 'Simic Hybrid'),
        ('siren', 'Siren'),
        ('tabaxi', 'Tabaxi'),
        ('thri_kreen', 'Thri-kreen'),
        ('tiefling', 'Tiefling'),
        ('tortle', 'Tortle'),
        ('triton', 'Triton'),
        ('vampire', 'Vampire'),
        ('vedalken', 'Vedalken'),
        ('verdan', 'Verdan'),
        ('viashino', 'Viashino'),
        ('warforged', 'Warforged'),
        ('yuan_ti', 'Yuan-ti'),
        ('yuan_ti_pureblood', 'Yuan-ti Pureblood'),
    ]

    # Common
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=50, choices=RACE_CHOICES)
    classes = models.ManyToManyField(CharacterClass, related_name='characters')
    level = models.IntegerField(default=1)
    input_method = models.CharField(max_length=20, choices=INPUT_METHOD_CHOICES, default='manual')
    created_at = models.DateTimeField(default=timezone.now)
    
    
    hit_points = models.IntegerField(default=10)
    armor_class = models.IntegerField(default=10)
    speed = models.IntegerField(default=30)  # Speed in feet per round
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)

    # Abilities
    proficiency_bonus = models.IntegerField(default=2)
    inspiration = models.BooleanField(default=False)

    # Features & Traits
    features_and_traits = models.TextField(blank=True)

    # Equipment
    equipment = models.TextField(blank=True)

    # Inventory
    inventory = models.TextField(blank=True)

    # Actions
    actions = models.TextField(blank=True)

    # Bonus Actions
    bonus_actions = models.TextField(blank=True)

    # Reactions
    reactions = models.TextField(blank=True)

    # Additional Stats
    initiative = models.IntegerField(default=0)
    passive_perception = models.IntegerField(default=10)

    # Saving Throws
    saving_throws = models.TextField(blank=True)

    # Skills
    skills = models.TextField(blank=True)

    # Languages
    languages = models.TextField(blank=True)

    # Background
    background = models.CharField(max_length=100, blank=True)

    # Alignment
    alignment = models.CharField(max_length=20, blank=True)

    # Experience
    experience_points = models.IntegerField(default=0)

    # Owner (each player character should prob be associated with a user)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Set the default owner to the first user in the database

    # Created Date
    created_at = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.name

    def get_total_ability_score(self):
        """Calculate the total ability score based on individual attributes."""
        return self.strength + self.dexterity + self.constitution + self.intelligence + self.wisdom + self.charisma

    def get_modifier(self, attribute_score):
        """Calculate the ability modifier for a given attribute score."""
        return (attribute_score - 10) // 2
