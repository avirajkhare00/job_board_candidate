# Generated by Django 2.1.5 on 2019-02-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_primaryskills_secondaryskills'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeDegrees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_degree_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=200)),
                ('slug_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CollegeSpecializations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_specialization_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=200)),
                ('slug_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='IndustryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry_type_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
