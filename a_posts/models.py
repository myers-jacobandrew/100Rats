from django.db import models
from django.utils import timezone
import uuid


'''
---- Basic Model Syntax ----
class Post(models.Model):
    title = models.CharField(max_length=500)
    image = models.URLField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
     
    def __str__(self):
        return str(self.title)
'''


class Monster(models.Model):
    # Common fields
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=20,null=True,blank=True)
    creature_type = models.CharField(max_length=20,null=True,blank=True)
    alignment = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)  
    
    # Stats
    armor_class = models.IntegerField(null=True, blank=True)
    hit_points = models.PositiveIntegerField(null=True, blank=True)
    speed = models.CharField(max_length=50)
    
    # Abilities
    strength = models.IntegerField(null=True, blank=True)
    dexterity = models.IntegerField(null=True, blank=True)
    constitution = models.IntegerField(null=True, blank=True)
    intelligence = models.IntegerField(null=True, blank=True)
    wisdom = models.IntegerField(null=True, blank=True)
    charisma = models.IntegerField(null=True, blank=True)
    
    # Saving Throws
    saving_throws = models.TextField(null=True,blank=True)
    
    # Skills
    skills = models.TextField(null=True,blank=True)
    
    # Damage Resistances and Immunities
    damage_resistances = models.TextField(null=True,blank=True)
    damage_immunities = models.TextField(null=True,blank=True)
    condition_immunities = models.TextField(null=True,blank=True)
    
    # Senses
    senses = models.TextField(null=True,blank=True)
    
    # Languages
    languages = models.TextField(null=True,blank=True)
    
    # Challenge and XP
    challenge_rating = models.DecimalField(max_digits=3, decimal_places=1,null=True, blank=True)
    experience_points = models.IntegerField(null=True, blank=True)
    
    # Special, Legendary, and Lair Actions
    special_abilities = models.TextField(null=True,blank=True)
    special_abilities_count = models.IntegerField(null=True, blank=True)
    
    #Spells
    # To-do
        
    # Actions
    actions = models.TextField(null=True, blank=True)
    
    # Extras
    raw_stat_block = models.TextField(blank=True)
    
    def __str__(self):
        return self.name



class Spell(models.Model):
    SPELL_TYPES = [
        ('DD', 'Damage Dealing'),
        ('HL', 'Healing'),
        ('UT', 'Utility'),
        ('OT', 'Other'),
    ]
    
    spell_name = models.CharField(max_length=100)
    spell_type = models.CharField(max_length=2, choices=SPELL_TYPES)
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




class PlayerCharacter(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    hit_points = models.IntegerField(default=10)
    armor_class = models.IntegerField(default=10)
    speed = models.IntegerField(default=30)  # Speed in feet per round
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)


    # Actions
    actions = models.TextField(blank=True)
    
    # Bonus Actions
    bonus_actions = models.TextField(blank=True)
    
        
    def __str__(self):
        return self.name