from django.shortcuts import render, redirect

from q.models import Instance, Character


def scan_admin(request, instance_slug, instance_secret):
    instance = Instance.objects.filter(slug=instance_slug).first()
    if instance is None:
        data = {'reason': "cette instance de jeu n'existe pas"}
        return render(request, 'error.html', data)

    if instance.secret != instance_secret:
        data = {'reason': "vous n'êtes pas autorisé à effectuer cette opération"}
        return render(request, 'error.html', data)

    displayed_code, has_a_new_character_been_revealed = instance.scan(None) 

    data = {
        'displayed_code': displayed_code,
        'instance_color': instance.color,
        'reset_url': f"/reset/{instance_slug}/{instance_secret}",
        'reload_url': f"/scan_admin/{instance_slug}/{instance_secret}",
    }
    return render(request, 'scan_admin.html', data)


def reset(request, instance_slug, instance_secret):
    instance = Instance.objects.filter(slug=instance_slug).first()

    if instance is None:
        data = {'reason': "cette instance de jeu n'existe pas"}
        return render(request, 'error.html', data)

    if instance.secret != instance_secret:
        data = {'reason': "vous n'êtes pas autorisé à effectuer cette opération"}
        return render(request, 'error.html', data)

    instance.reset()
    return redirect(f"/scan_admin/{instance_slug}/{instance_secret}")


def scan(request, instance_slug, scan_slug):
    instance = Instance.objects.filter(slug=instance_slug).first()
    if instance is None:
        data = {'reason': "cette instance de jeu n'existe pas"}
        return render(request, 'error.html', data)

    displayed_code, has_new_character_been_revealed = instance.scan(scan_slug)
    data = {
        'displayed_code': displayed_code,
        'has_new_character_been_revealed': has_new_character_been_revealed,
        'instance_color': instance.color,
    }
    return render(request, 'scan.html', data)
