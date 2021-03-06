# Generated by Django 3.1 on 2020-08-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_bazaar_app', '0009_auto_20200819_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='discription',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.IntegerField(choices=[(1, 'Horror'), (7, 'Animowany'), (8, 'Kryminalny'), (5, 'Akcja'), (4, 'Dramat'), (0, 'Inne'), (6, 'Katastroficzny'), (2, 'Komedia'), (3, 'Sci-fi')], null=True),
        ),
    ]
