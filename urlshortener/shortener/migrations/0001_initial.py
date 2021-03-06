# Generated by Django 4.1.dev20211116102130 on 2021-12-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Short_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=250)),
                ('short_url', models.CharField(max_length=15, unique=True)),
                ('accessed_times', models.PositiveIntegerField(default=0)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
