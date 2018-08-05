# Generated by Django 2.0.7 on 2018-08-05 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('witness_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='witness',
            name='relationship',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='witness',
            name='coordinator_assignee',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='witness',
            name='coordinator_department',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='witness',
            name='created_by',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='witness',
            name='created_date',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='witness',
            name='email',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='witness',
            name='manager_assignee',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='witness',
            name='mechanism',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='witness',
            name='witness_type',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]