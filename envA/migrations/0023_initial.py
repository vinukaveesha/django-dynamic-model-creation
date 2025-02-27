# Generated by Django 5.1.5 on 2025-02-27 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('envA', '0022_delete_owners_delete_phbas_inventory'),
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
        migrations.CreateModel(
            name='Phbas_inventory',
            fields=[
                ('INVENTORY_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('APPROVEDBY', models.CharField(max_length=255)),
                ('APPROVED_BY_ID', models.CharField(max_length=255)),
                ('APPROVEDON', models.CharField(max_length=255)),
                ('CREATEDBY', models.CharField(max_length=255)),
                ('CREATED_BY_ID', models.CharField(max_length=255)),
                ('CREATEDON', models.CharField(max_length=255)),
                ('GROUPID', models.CharField(max_length=255)),
                ('HOSPITALID', models.CharField(max_length=255)),
                ('ISACTIVE', models.CharField(max_length=255)),
                ('ISDEFAULT', models.CharField(max_length=255)),
                ('LOCATION_ID', models.CharField(max_length=255)),
                ('MODIFIEDBY', models.CharField(max_length=255)),
                ('MODIFIED_BY_ID', models.CharField(max_length=255)),
                ('MODIFIEDON', models.CharField(max_length=255)),
                ('ROWVERSION', models.CharField(max_length=255)),
                ('ADDITIONAL_DATA', models.CharField(max_length=255)),
                ('BATCH', models.CharField(max_length=255)),
                ('CATEGORY_ID', models.CharField(max_length=255)),
                ('CRASH_CART', models.CharField(max_length=255)),
                ('DRUG_ID', models.CharField(max_length=255)),
                ('DRUG_NAME', models.CharField(max_length=255)),
                ('DRUG_NAME_PLAIN_TEXT', models.CharField(max_length=255)),
                ('ERP_CODE', models.CharField(max_length=255)),
                ('EXPIRY_DATE', models.CharField(max_length=255)),
                ('IV', models.CharField(max_length=255)),
                ('LOCATION_NAME', models.CharField(max_length=255)),
                ('LOCATION_TYPE_ALIAS', models.CharField(max_length=255)),
                ('LOT_NO', models.CharField(max_length=255)),
                ('PRICE', models.CharField(max_length=255)),
                ('QIS', models.CharField(max_length=255)),
                ('RDFE', models.CharField(max_length=255)),
                ('REMAIN_QTY', models.CharField(max_length=255)),
                ('STATUS', models.CharField(max_length=255)),
                ('UNIT_PRICE', models.CharField(max_length=255)),
                ('BARCODE', models.CharField(max_length=255)),
                ('UOM_ID', models.CharField(max_length=255)),
                ('UOM_VALUE', models.CharField(max_length=255)),
                ('FORMULARY_NAME', models.CharField(max_length=255)),
                ('FORMULARY_PLAIN_TEXT', models.CharField(max_length=255)),
                ('FORMULARY_CODE', models.CharField(max_length=255)),
                ('ERP_VENDOR', models.CharField(max_length=255)),
                ('VENDOR_ITEM_CODE', models.CharField(max_length=255)),
                ('IS_ERP_BRAND', models.CharField(max_length=255)),
                ('GTIN', models.CharField(max_length=255)),
                ('SUB_INVENTORY_CODE', models.CharField(max_length=255)),
                ('HOLD_QTY', models.CharField(max_length=255)),
                ('CREATED_BY', models.CharField(max_length=255)),
                ('CREATED_DATE', models.CharField(max_length=255)),
                ('EPISODE_ID', models.CharField(max_length=255)),
                ('HOSPITAL_GROUP_ID', models.CharField(max_length=255)),
                ('HOSPITAL_ID', models.CharField(max_length=255)),
                ('MODIFIED_BY', models.CharField(max_length=255)),
                ('GENERIC_FORMULARY_ID', models.CharField(max_length=255)),
                ('ACTIVE_INVENTORY', models.CharField(max_length=255)),
                ('SECONDARY_CONVERSION_FACTOR', models.CharField(max_length=255)),
                ('SECONDARY_UOM_ID', models.CharField(max_length=255)),
                ('SECONDARY_UOM_VALUE', models.CharField(max_length=255)),
            ],
            options={
                'db_table': '"PH_PHARMACY"."PHBAS_INVENTORY"',
                'managed': False,
            },
        ),
    ]
