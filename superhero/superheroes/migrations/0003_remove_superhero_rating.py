# Generated by Django 3.2.5 on 2021-07-30 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superheroes', '0002_superhero_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superhero',
            name='rating',
        ),
    ]