# Generated by Django 4.1.1 on 2022-10-01 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0008_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='viewer.director'),
        ),
    ]
