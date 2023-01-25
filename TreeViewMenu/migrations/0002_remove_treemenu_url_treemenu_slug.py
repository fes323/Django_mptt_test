# Generated by Django 4.1.5 on 2023-01-24 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TreeViewMenu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treemenu',
            name='url',
        ),
        migrations.AddField(
            model_name='treemenu',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True, verbose_name='slug'),
        ),
    ]