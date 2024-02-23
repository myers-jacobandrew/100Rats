from django.contrib import admin
from .models import *

#admin.site.register()
admin.site.register(Spell)
admin.site.register(PlayerCharacter)

#Fields to display in admin panel
class MonsterAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'alignment', 'armor_class', 'hit_points', 'created_at'] 

admin.site.register(Monster, MonsterAdmin)