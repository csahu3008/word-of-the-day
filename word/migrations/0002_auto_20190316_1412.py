# Generated by Django 2.1 on 2019-03-16 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_words',
            name='Antonyms',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='daily_words',
            name='Meaning',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='daily_words',
            name='Synonyms',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='daily_words',
            name='Word',
            field=models.CharField(max_length=20),
        ),
    ]
