# Generated by Django 5.1.5 on 2025-02-25 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand_mapping_tracker',
            fields=[
                ('brand_mapping_tracker_id', models.IntegerField(primary_key=True, serialize=False)),
                ('approvedby', models.CharField(max_length=255)),
                ('approved_by_id', models.CharField(max_length=255)),
                ('approvedon', models.CharField(max_length=255)),
                ('createdby', models.CharField(max_length=255)),
                ('created_by_id', models.CharField(max_length=255)),
                ('createdon', models.CharField(max_length=255)),
                ('groupid', models.CharField(max_length=255)),
                ('hospitalid', models.CharField(max_length=255)),
                ('isactive', models.CharField(max_length=255)),
                ('isdefault', models.CharField(max_length=255)),
                ('location_id', models.CharField(max_length=255)),
                ('modifiedby', models.CharField(max_length=255)),
                ('modified_by_id', models.CharField(max_length=255)),
                ('modifiedon', models.CharField(max_length=255)),
                ('rowversion', models.CharField(max_length=255)),
                ('brand_summary_details', models.CharField(max_length=255)),
                ('erp_code', models.CharField(max_length=255)),
                ('status_alias', models.CharField(max_length=255)),
            ],
            options={
                'db_table': '"PH_PHARMACY"."BRAND_MAPPING_TRACKER"',
                'managed': False,
            },
        ),
    ]
