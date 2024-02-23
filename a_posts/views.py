# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from a_core.scripts.stat_parser import parse_stat_block


def home_view(request):
    title = 'Welcome'
    monsters = Monster.objects.all()
    return render(request, 'a_posts/home.html', {'title': title, 'monsters': monsters})
from .models import Monster

def create_monster_view(request):
    if request.method == 'POST':
        # Check if the input method is automatic
        input_method = request.POST.get('input_method')
        print("Input method:", input_method)

        if input_method == 'automatic':
            form = AutomaticMonsterForm(request.POST)
        else:
            form = ManualMonsterForm(request.POST)

        if form.is_valid():
            print("Form is valid")

            if input_method == 'automatic':
                print("Automatic mode:")
                # Parse the stats from the raw text field
                raw_text = form.cleaned_data.get('raw_stat_block')
                print("Raw text:", raw_text)

                # Extract name from the raw text
                name = raw_text.split('\n')[0].strip()
                form.cleaned_data['name'] = name
                print("Extracted name:", name)

                # Parse the stat block
                parsed_stats = parse_stat_block(raw_text)
                print("Parsed stats:", parsed_stats)

                # Update form data with parsed stats
                form.cleaned_data.update(parsed_stats)
                print("Stats have been automatically parsed")
                
            print("Form data after parsing:", form.cleaned_data)
          
          
          # Save the form instance directly if valid
            try:                
                monster = form.save(commit=False)
                # Add input_method to the monster instance
                monster.input_method = input_method

                # Update the instance with parsed stats
                monster.__dict__.update(parsed_stats)
                print("Monster before saving:", monster.__dict__)
                
                monster.save()
                print("Monster saved:", monster)
            except Exception as e:
                print("Error saving monster:", e)

            # Redirect to appropriate page based on input method
            if input_method == 'automatic':
                return redirect('automatic-data-entered')
            else:
                return redirect('manual-data-entered')
        else:
            print("Form is not valid")
            print("Form errors:", form.errors)
    else:
        # If it's a GET request or the form is not valid, render the form page with a new form instance
        form = ManualMonsterForm()

    return render(request, 'a_posts/create_monster.html', {'form': form})


#                # Add input_method to the monster instance
#                monster.input_method = input_method
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