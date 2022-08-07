from django.contrib import admin

from q.models import Instance, InstanceForm, Character, CharacterForm


class InstanceAdmin(admin.ModelAdmin):
    form = InstanceForm
    list_display = (
        'slug',
        'color',
        'secret',
    )
    search_fields = (
        'slug',
        'color',
        'secret',
    )


class CharacterAdmin(admin.ModelAdmin):
    form = CharacterForm
    list_display = (
        'instance',
        'order',
        'value',
        'slug',
        'revealed',
    )
    search_fields = (
        'instance',
        'order',
        'value',
        'slug',
        'revealed'
    )


admin.site.register(Instance, InstanceAdmin)
admin.site.register(Character, CharacterAdmin)
