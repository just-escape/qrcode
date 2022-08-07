from django.db import models
from django import forms


class Instance(models.Model):
    slug = models.CharField(max_length=16)
    color = models.CharField(max_length=512)
    secret = models.CharField(max_length=512)

    def reset(self):
        code = Character.objects.filter(instance=self).all()
        for char in code:
            char.revealed = char.revealed_by_default
            char.save()

    def scan(self, slug):
        code = Character.objects.filter(instance=self).order_by('order').all()

        displayed_code = []
        for char in code:
            if char.revealed:
                displayed_code.append({'char': char.value, 'revealed_by_this_scan': False})
            elif char.slug == slug:
                char.revealed = True
                char.save()
                displayed_code.append({'char': char.value, 'revealed_by_this_scan': True})
            else:
                displayed_code.append({'char': '_', 'revealed_by_this_scan': False})

        has_a_new_character_been_revealed = any(c['revealed_by_this_scan'] for c in displayed_code)
        return displayed_code, has_a_new_character_been_revealed


class InstanceForm(forms.ModelForm):
    class Meta:
        model = Instance
        fields = '__all__'


class Character(models.Model):
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    order = models.IntegerField()
    value = models.CharField(max_length=1)
    slug = models.CharField(max_length=512)
    revealed = models.BooleanField()
    revealed_by_default = models.BooleanField()


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'
