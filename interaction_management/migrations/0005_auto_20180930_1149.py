# Generated by Django 2.0.7 on 2018-09-30 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interaction_management', '0004_auto_20180807_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='parent_id',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]