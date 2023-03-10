# Generated by Django 4.1.6 on 2023-02-09 14:43

from django.db import migrations, models
import json_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.CharField(max_length=200)),
                ('default_language', models.CharField(max_length=100)),
                ('titles', json_field.fields.JSONField(blank=True, default='null', help_text='Enter a valid JSON object', max_length=5000)),
            ],
        ),
    ]
