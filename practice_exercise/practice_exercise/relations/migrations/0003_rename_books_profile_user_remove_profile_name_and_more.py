# Generated by Django 4.2.11 on 2025-02-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0002_rename_author_book_authors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='books',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=''),
        ),
    ]
