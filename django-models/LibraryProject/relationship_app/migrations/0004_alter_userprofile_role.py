# Generated by Django 5.1.6 on 2025-02-23 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0003_userprofile_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('librarian', 'Librarian'), ('member', 'Member')], max_length=50),
        ),
    ]
