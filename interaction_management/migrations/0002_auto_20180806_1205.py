# Generated by Django 2.0.7 on 2018-08-06 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interaction_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interaction',
            old_name='primary_phone',
            new_name='interaction_date',
        ),
        migrations.AddField(
            model_name='interaction',
            name='phone',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
