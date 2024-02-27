from django.contrib import admin
from .models import *

#admin.site.register()


#Fields to display in admin panel for Monster Table
class MonsterAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'alignment', 'armor_class', 'hit_points', 'created_at', 'input_method'] 



#Fields to display in admin panel for Player Character Table
class PlayerCharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'input_method'] 




#Fields to display in admin panel for Spell Table
class SpellAdmin(admin.ModelAdmin):
    list_display = ['spell_name', 'created_at', 'input_method'] 




admin.site.register(Monster, MonsterAdmin)
admin.site.register(Spell, SpellAdmin)
admin.site.register(PlayerCharacter, PlayerCharacterAdmin)