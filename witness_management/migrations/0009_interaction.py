# Generated by Django 2.0.7 on 2018-10-01 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('witness_management', '0008_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('parent_id', models.CharField(blank=True, max_length=40, null=True)),
                ('interaction_number', models.CharField(blank=True, max_length=20, null=True)),
                ('direction', models.CharField(blank=True, max_length=40, null=True)),
                ('interaction_type', models.CharField(blank=True, max_length=40, null=True)),
                ('interaction_method', models.CharField(blank=True, max_length=40, null=True)),
                ('interactor', models.CharField(blank=True, max_length=40, null=True)),
                ('summary', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=60, null=True)),
                ('phone', models.CharField(blank=True, max_length=60, null=True)),
                ('email', models.CharField(blank=True, max_length=40, null=True)),
                ('status', models.CharField(blank=True, max_length=40, null=True)),
                ('created_by', models.CharField(blank=True, max_length=60, null=True)),
                ('created_date', models.CharField(blank=True, max_length=60, null=True)),
                ('interaction_date', models.CharField(blank=True, max_length=60, null=True)),
                ('relationship', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
    ]
