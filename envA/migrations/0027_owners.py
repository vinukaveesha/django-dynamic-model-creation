# Generated by Django 5.1.5 on 2025-02-27 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envA', '0026_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
            ],
            options={
                'db_table': '"public"."owners"',
                'managed': False,
            },
        ),
    ]
