# Generated by Django 3.2 on 2022-03-18 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.book')),
            ],
        ),
    ]
