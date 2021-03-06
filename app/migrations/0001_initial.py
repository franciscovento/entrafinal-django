# Generated by Django 3.2 on 2022-03-23 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=16)),
                ('status', models.CharField(choices=[('active', 'Active'), ('closed', 'Closed'), ('cancelled', 'Cancelled'), ('blacklisted', 'Blacklisted'), ('none', 'None')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.FloatField()),
                ('publication_date', models.DateField()),
                ('author', models.ManyToManyField(to='app.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rack_numer', models.CharField(choices=[('primary', 'PRIMARY'), ('second', 'SECOND'), ('third', 'THIRD'), ('quarter', 'QUARTER'), ('fifth', 'FIFTH'), ('sexth', 'SIXTH')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.account')),
            ],
            bases=('app.account',),
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=20)),
                ('is_referenc_only', models.BooleanField(default=False)),
                ('borrowed', models.DateField()),
                ('due_date', models.DateField()),
                ('format_book', models.CharField(choices=[('hardcover', 'Hardcover'), ('paperback', 'Paperback'), ('audiobook', 'Audiobook'), ('ebook', 'Ebook'), ('newspaper', 'Newspaper'), ('magazine', 'Magazine'), ('journal', 'Journal')], max_length=15)),
                ('status', models.CharField(choices=[('available', 'Available'), ('reserved', 'Reserved'), ('loaned', 'Loaned'), ('lost', 'Lost')], max_length=15)),
                ('date_of_purchase', models.DateField()),
                ('book_reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.book')),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.rack')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='app.Category'),
        ),
    ]
