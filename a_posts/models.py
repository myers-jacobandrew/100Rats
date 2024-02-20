from django.db import models
import uuid


'''class Post(models.Model):
    title = models.CharField(max_length=500)
    image = models.URLField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
     
    def __str__(self):
        return str(self.title)
   '''
    
from django.db import models

class Monster(models.Model):
    # Common fields
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=20)
    creature_type = models.CharField(max_length=20)
    alignment = models.CharField(max_length=20)
    
    # Stats
    armor_class = models.IntegerField(null=True)
    hit_points = models.PositiveIntegerField(null=True)
    speed = models.CharField(max_length=50)
    
    # Abilities
    strength = models.IntegerField(null=True)
    dexterity = models.IntegerField(null=True)
    constitution = models.IntegerField(null=True)
    intelligence = models.IntegerField(null=True)
    wisdom = models.IntegerField(null=True)
    charisma = models.IntegerField(null=True)
    
    # Saving Throws
    saving_throws = models.TextField(blank=True)
    
    # Skills
    skills = models.TextField(blank=True)
    
    # Damage Resistances and Immunities
    damage_resistances = models.TextField(blank=True)
    damage_immunities = models.TextField(blank=True)
    condition_immunities = models.TextField(blank=True)
    
    # Senses
    senses = models.TextField(blank=True)
    
    # Languages
    languages = models.TextField(blank=True)
    
    # Challenge and XP
    challenge_rating = models.DecimalField(max_digits=3, decimal_places=1)
    experience_points = models.IntegerField(null=True)
    
    # Special Abilities
    special_abilities = models.TextField(blank=True)
    special_abilities_count = models.IntegerField(null=True)
    
    # Actions
    actions = models.TextField(blank=True)
    
    #extras
    raw_stat_block = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
