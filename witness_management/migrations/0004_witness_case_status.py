# Generated by Django 2.0.7 on 2018-08-05 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('witness_management', '0003_auto_20180805_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='witness',
            name='case_status',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
