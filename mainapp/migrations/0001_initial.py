# Generated by Django 3.2.2 on 2021-05-18 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('twitterid', models.CharField(max_length=20)),
            ],
        ),
    ]
