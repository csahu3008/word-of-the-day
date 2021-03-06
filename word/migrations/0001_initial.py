# Generated by Django 2.1 on 2019-03-16 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_posted', models.DateField(auto_now=True)),
                ('Word', models.TextField(max_length=20)),
                ('Meaning', models.TextField(max_length=100)),
                ('Synonyms', models.TextField(max_length=80)),
                ('Antonyms', models.TextField(max_length=80)),
                ('examples', models.TextField()),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
