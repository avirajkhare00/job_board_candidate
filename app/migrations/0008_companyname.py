# Generated by Django 2.1.5 on 2019-02-16 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_indiancityname'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('company_name_slug', models.CharField(max_length=200)),
            ],
        ),
    ]
