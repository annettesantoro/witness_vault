# Generated by Django 2.0.7 on 2018-10-02 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('witness_management', '0010_auto_20181001_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='modified_by',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='modified_date',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='interaction',
            name='modified_by',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='interaction',
            name='modified_date',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='witness',
            name='modified_by',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='witness',
            name='modified_date',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
