# Generated by Django 3.2 on 2022-03-23 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookitem',
            old_name='books',
            new_name='Rack_rereference',
        ),
    ]