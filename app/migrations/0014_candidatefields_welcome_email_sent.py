# Generated by Django 2.1.5 on 2019-03-09 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20190224_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatefields',
            name='welcome_email_sent',
            field=models.BooleanField(default=False),
        ),
    ]