# Generated by Django 4.1.6 on 2023-02-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0005_articles_delete_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.JSONField(default=dict, verbose_name='Article_Title'),
        ),
    ]
