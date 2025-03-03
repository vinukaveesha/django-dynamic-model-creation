# Generated by Django 5.1.5 on 2025-02-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envA', '0014_owners_delete_vet_specialties'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SETUPID', models.CharField(max_length=255)),
                ('PROJECTID', models.CharField(max_length=255)),
                ('ITEMID', models.CharField(max_length=255)),
                ('ITEMDESCRIPTION', models.CharField(max_length=255)),
                ('ITEMDESCRIPTIONN', models.CharField(max_length=255)),
                ('ITEMCATEGORYID', models.CharField(max_length=255)),
                ('ITEMGROUPID', models.CharField(max_length=255)),
                ('ITEMSUBGROUPID', models.CharField(max_length=255)),
                ('GENERICNAMEID', models.CharField(max_length=255)),
                ('ALIAS', models.CharField(max_length=255)),
                ('ALIASN', models.CharField(max_length=255)),
                ('PRINTNAME', models.CharField(max_length=255)),
                ('ITEMUNITS', models.CharField(max_length=255)),
                ('ITEMUOM', models.CharField(max_length=255)),
                ('PURCHASEPRICE', models.CharField(max_length=255)),
                ('SELLINGPRICE', models.CharField(max_length=255)),
                ('PROFITMARGIN', models.CharField(max_length=255)),
                ('MAXIMUMDISCOUNT', models.CharField(max_length=255)),
                ('ORDERINGUOM', models.CharField(max_length=255)),
                ('DESPENSINGUOM', models.CharField(max_length=255)),
                ('MAXLEVEL', models.CharField(max_length=255)),
                ('MINLEVEL', models.CharField(max_length=255)),
                ('REORDERLEVEL', models.CharField(max_length=255)),
                ('LEADTIME', models.CharField(max_length=255)),
                ('SALESTAX', models.CharField(max_length=255)),
                ('VAT', models.CharField(max_length=255)),
                ('REGIONTAX', models.CharField(max_length=255)),
                ('MAXDOSAGE', models.CharField(max_length=255)),
                ('STRENGTH', models.CharField(max_length=255)),
                ('THERAPEUTICCATEGORYID', models.CharField(max_length=255)),
                ('ISITEMSTOPROL', models.CharField(max_length=255)),
                ('ISITEMUNITREG', models.CharField(max_length=255)),
                ('ISDRUGINTERACTION', models.CharField(max_length=255)),
                ('ISIMPORTED', models.CharField(max_length=255)),
                ('SELLINGMOVEMENT', models.CharField(max_length=255)),
                ('INPSERVICECHARGES', models.CharField(max_length=255)),
                ('ISINPSERVICECHARGES', models.CharField(max_length=255)),
                ('MEDICATIONDAYS', models.CharField(max_length=255)),
                ('STATUS', models.CharField(max_length=255)),
                ('CREATEDBY', models.CharField(max_length=255)),
                ('EDITEDBY', models.CharField(max_length=255)),
                ('ROWVER', models.CharField(max_length=255)),
                ('VENDORID', models.CharField(max_length=255)),
                ('DEFAULTDOSE', models.CharField(max_length=255)),
                ('USESUPPLIERBARCODE', models.CharField(max_length=255)),
                ('SUPPLIERBARCODE', models.CharField(max_length=255)),
                ('ORACLE_ITEM_CODE', models.CharField(max_length=255)),
                ('ORACLE_M_UOM', models.CharField(max_length=255)),
                ('ORACLE_S_UOM', models.CharField(max_length=255)),
                ('ISNARCOTIC', models.CharField(max_length=255)),
                ('ISANTIBIOTIC', models.CharField(max_length=255)),
                ('ISIVMEDICINE', models.CharField(max_length=255)),
                ('DEFAULTDIRECTION', models.CharField(max_length=255)),
                ('DEFAULTROUTEID', models.CharField(max_length=255)),
                ('IVSTABILITY', models.CharField(max_length=255)),
                ('IVRATE', models.CharField(max_length=255)),
                ('IVDILUENTTYPE', models.CharField(max_length=255)),
                ('IVDILUENTVOLUME', models.CharField(max_length=255)),
                ('IVDILUENTLINE', models.CharField(max_length=255)),
                ('ACCESSLEVEL', models.CharField(max_length=255)),
                ('PRESCRIPTIONALLOWED', models.CharField(max_length=255)),
                ('ECOMMERCECATEGORYID', models.CharField(max_length=255)),
                ('PRESCRIBINGCLASSIFICATIONID', models.CharField(max_length=255)),
                ('OUTPATIENTDEFAULTDAYS', models.CharField(max_length=255)),
                ('OUTPATIENTDEFAULTQUANTITY', models.CharField(max_length=255)),
                ('ITEMBRANDID', models.CharField(max_length=255)),
                ('UNPRIVILEGEDPRESCRIBERGRACEPERIOD', models.CharField(max_length=255)),
                ('ISCHARGEIVADMIXTURE', models.CharField(max_length=255)),
                ('TAXPERCENTAGE', models.CharField(max_length=255)),
                ('TAXABLESTATUS', models.CharField(max_length=255)),
                ('ISPROMOTIONITEM', models.CharField(max_length=255)),
                ('DEFAULTCOMMENTS', models.CharField(max_length=255)),
                ('ISCHEMODRUG', models.CharField(max_length=255)),
                ('ISHIGHALERT', models.CharField(max_length=255)),
                ('ISSIGLETIMEDISPENSING', models.CharField(max_length=255)),
                ('DDCCODESTATUS', models.CharField(max_length=255)),
                ('ITEMINSURANCECATEGORYID', models.CharField(max_length=255)),
                ('SFDACODE', models.CharField(max_length=255)),
                ('ACTIVITYTYPE', models.CharField(max_length=255)),
                ('IVMEDICINETYPE', models.CharField(max_length=255)),
                ('ALERTCONSIDERATION', models.CharField(max_length=255)),
                ('ISNEEDEARLYPREPARATION', models.CharField(max_length=255)),
                ('ISNEEDWITNESSFORMRA', models.CharField(max_length=255)),
                ('EARLYPREPARATIONTIME', models.CharField(max_length=255)),
                ('SCIENTIFICID', models.CharField(max_length=255)),
                ('DDCEXPIRY', models.CharField(max_length=255)),
                ('ISOPDPRESCRIPTIONALLOWED', models.CharField(max_length=255)),
                ('NPHIESCODESYSTEM', models.CharField(max_length=255)),
                ('ISSFDAENABLEDQRCODEALLOWED', models.CharField(max_length=255)),
                ('FORMULARYID', models.CharField(max_length=255)),
                ('ISBRAND', models.CharField(max_length=255)),
                ('ISUNREPLACEABLE', models.CharField(max_length=255)),
                ('DISPENSESEQ', models.CharField(max_length=255)),
            ],
            options={
                'db_table': '"PH_PHARMACY"."PHARMACY_ITEM"',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Owners',
        ),
    ]
