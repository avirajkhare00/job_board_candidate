# Generated by Django 2.1.5 on 2019-02-14 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_usergeneratedskills'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndianCityName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=200)),
                ('city_value', models.CharField(max_length=200)),
            ],
        ),
    ]
