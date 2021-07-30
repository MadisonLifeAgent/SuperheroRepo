# Generated by Django 3.2.5 on 2021-07-30 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('alter_ego', models.CharField(max_length=50)),
                ('primary_superpower', models.CharField(max_length=50)),
                ('secondary_superpower', models.CharField(max_length=50)),
                ('catchphrase', models.CharField(max_length=50)),
            ],
        ),
    ]
