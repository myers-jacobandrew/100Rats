# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Monster
from .forms import ManualMonsterForm, AutomaticMonsterForm
from a_core.scripts.stat_parser import StatBlockParser


def home_view(request):
    title = 'Welcome'
    monsters = Monster.objects.all()
    return render(request, 'a_posts/home.html', {'title': title, 'monsters': monsters})
from .models import Monster


def create_monster_view(request):
    if request.method == 'POST':
        # Check if the input method is automatic
        input_method = request.POST.get('input_method')

        if input_method == 'automatic':
            form = AutomaticMonsterForm(request.POST)
        else:
            form = ManualMonsterForm(request.POST)

        if form.is_valid():
            # If the input method is automatic, parse the stats from the raw text field
            if input_method == 'automatic':
                raw_text = form.cleaned_data.get('raw_stat_block')
                parser = StatBlockParser()
                parsed_stats = parser.parse_stat_block(raw_text)

                # Update form data with parsed stats
                form.cleaned_data.update(parsed_stats)

                
                try:
                    # Create a new Monster instance
                    monster = form.save(commit=False)

                    # Assign each parsed stat to the corresponding field in the Monster model
                    monster.name = parsed_stats.get('Name')
                    monster.size = parsed_stats.get('Size')
                    monster.alignment = parsed_stats.get('Alignment')
                    monster.armor_class = parsed_stats.get('Armor Class')
                    monster.hit_points = parsed_stats.get('Hit Points')
                    monster.speed = parsed_stats.get('Speed')
                    monster.strength = parsed_stats.get('Abilities', {}).get('STR', [None])[0]
                    monster.dexterity = parsed_stats.get('Abilities', {}).get('DEX', [None])[0]
                    monster.constitution = parsed_stats.get('Abilities', {}).get('CON', [None])[0]
                    monster.intelligence = parsed_stats.get('Abilities', {}).get('INT', [None])[0]
                    monster.wisdom = parsed_stats.get('Abilities', {}).get('WIS', [None])[0]
                    monster.charisma = parsed_stats.get('Abilities', {}).get('CHA', [None])[0]
                    monster.saving_throws = parsed_stats.get('Saving Throws')
                    monster.skills = parsed_stats.get('Skills')
                    monster.damage_resistances = parsed_stats.get('Damage Resistances')
                    monster.damage_immunities = parsed_stats.get('Damage Immunities')
                    monster.condition_immunities = parsed_stats.get('Condition Immunities')
                    monster.senses = parsed_stats.get('Senses')
                    monster.languages = parsed_stats.get('Languages')
                    monster.challenge_rating = parsed_stats.get('Challenge Rating')
                    monster.experience_points = parsed_stats.get('Experience Points')
                    
                    # Combine 'Actions' and 'Legendary Actions' into 'special_abilities'
                    actions = parsed_stats.get('Actions', [])
                    legendary_actions = parsed_stats.get('Legendary Actions', [])
                    combined_special_abilities = []
                    combined_special_abilities.extend(actions)
                    combined_special_abilities.extend(legendary_actions)
                    monster.special_abilities = combined_special_abilities

                    # Count the number of special abilities
                    monster.special_abilities_count = len(combined_special_abilities)

                    monster.raw_stat_block = raw_text

                    monster.save()

                except Exception as e:
                    print("Error saving monster:", e)
            # Redirect to appropriate page based on input method
            if input_method == 'automatic':
                return redirect('automatic-data-entered')
            else:
                return redirect('manual-data-entered')
    else:
        # If it's a GET request or the form is not valid, render the form page with a new form instance
        form = ManualMonsterForm()

    return render(request, 'a_posts/create_monster.html', {'form': form})


def view_all_monsters(request):
    monsters = Monster.objects.all()
    return render(request, 'a_posts/view_all_monsters.html', {'monsters': monsters})

def manual_input_form_view(request):
    return render(request, 'a_posts/manual_input_form.html')

def automatic_input_form_view(request):
    return render(request, 'a_posts/automatic_input_form.html')
 
def automatic_data_entered_view(request):
    return render(request, 'automatic_data_entered.html')

def manual_data_entered_view(request):
    return render(request, 'manual_data_entered.html')