# Generated by Django 4.2.1 on 2024-08-31 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptom_checker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='symptoms',
            field=models.TextField(help_text='Comma-separated list of symptoms'),
        ),
    ]
