# Generated by Django 2.1.5 on 2019-02-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcategory',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobname',
            name='job_name_slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]