# Generated by Django 4.1.1 on 2022-10-22 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0015_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[['ACTION', 'ACTION'], ['COMEDY', 'COMEDY']], max_length=30),
        ),
    ]