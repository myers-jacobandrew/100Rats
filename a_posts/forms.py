# forms.py

from django import forms
from .models import Monster

class YourMonsterForm(forms.ModelForm):
    input_method = forms.ChoiceField(choices=[('manual', 'Manually Enter Stats'), ('automatic', 'Automatically Parse Stat Block')], label='Input Method')
    
    class Meta:
        model = Monster
        fields = ['name', 'size', 'creature_type', 'alignment', 'armor_class', 'hit_points', 'speed', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'saving_throws', 'skills', 'damage_resistances', 'damage_immunities', 'condition_immunities', 'senses', 'languages', 'challenge_rating', 'experience_points', 'special_abilities', 'special_abilities_count', 'actions', 'raw_stat_block']
        widgets = {
            'raw_stat_block': forms.Textarea(attrs={'rows': 10, 'cols': 40}),
        }
