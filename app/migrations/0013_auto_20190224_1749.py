# Generated by Django 2.1.5 on 2019-02-24 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20190217_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primaryskills',
            name='associated_to_job',
        ),
        migrations.RemoveField(
            model_name='secondaryskills',
            name='associated_to_primary_skill',
        ),
    ]
