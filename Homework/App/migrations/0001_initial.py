# Generated by Django 5.0.1 on 2024-01-04 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Publishing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('adres', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('caption', models.CharField(max_length=100)),
                ('img', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.category')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorPublishing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.author')),
                ('publishing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.publishing')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='publishing',
            field=models.ManyToManyField(through='App.AuthorPublishing', to='App.publishing'),
        ),
    ]
