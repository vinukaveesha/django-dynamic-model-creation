# Generated by Django 5.1.5 on 2025-02-26 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('envA', '0012_delete_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vet_specialties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vet_id', models.CharField(max_length=255)),
                ('specialty_id', models.CharField(max_length=255)),
            ],
            options={
                'db_table': '"public"."vet_specialties"',
                'managed': False,
            },
        ),
    ]
