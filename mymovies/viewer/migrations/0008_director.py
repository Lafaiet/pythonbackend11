# Generated by Django 4.1.1 on 2022-10-01 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0007_alter_movie_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_birth', models.DateField()),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
