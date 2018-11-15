# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-19 13:53
from __future__ import unicode_literals

from django.db import migrations
from django.db.models import Q


def mark_staff_profiles(apps, schema_editor):
    IdpProfile = apps.get_model('users', 'IdpProfile')
    # type 40 equals to IdpProfile.PROVIDER_LDAP
    ldap_idps = IdpProfile.objects.filter(primary=True, type=40)
    email_q = (Q(email__icontains='mozilla.com') | Q(email__icontains='getpocket.com') |
               Q(email__icontains='mozillafoundation.org') | Q(email__icontains='mozilla.org'))
    staff_idps = ldap_idps.filter(email_q)
    for idp in staff_idps:
        idp.profile.is_staff = True
        idp.save()


def backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_userprofile_is_staff'),
    ]

    operations = [
        migrations.RunPython(mark_staff_profiles, backwards),
    ]