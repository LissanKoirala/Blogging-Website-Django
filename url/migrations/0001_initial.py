# Generated by Django 3.0.8 on 2020-08-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('url', models.TextField()),
                ('short_url', models.TextField(null=True)),
            ],
        ),
    ]
