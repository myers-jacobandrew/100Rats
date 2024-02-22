# views.py

from django.shortcuts import render, redirect
from .models import Monster
from .forms import YourMonsterForm
from a_core.scripts.stat_parser import parse_stat_block


def home_view(request):
    title = 'Welcome'
    monsters = Monster.objects.all()
    return render(request, 'a_posts/home.html', {'title': title, 'monsters': monsters})

def create_monster_view(request):
    if request.method == 'POST':
        form = YourMonsterForm(request.POST)

        if form.is_valid():
            # Check if the form contains a raw_stat_block field
            if 'raw_stat_block' in form.cleaned_data:
                raw_stat_block = form.cleaned_data['raw_stat_block']
                # Parse the raw_stat_block
                parsed_data = parse_stat_block(raw_stat_block)
                # Update the form data with parsed data
                form = YourMonsterForm({**form.cleaned_data, **parsed_data})
            else:
                # If raw_stat_block is not present, continue as usual
                pass

            # Process and assign data to the Monster model
            monster = form.save(commit=False)
            # Save the monster instance
            monster.save()

            # Redirect to a success page or another view
            return redirect('success_page')

    else:
        form = YourMonsterForm()

    return render(request, 'a_posts/create_monster.html', {'form': form})

def view_all_monsters(request):
    monsters = Monster.objects.all()
    return render(request, 'a_posts/view_all_monsters.html', {'monsters': monsters})
