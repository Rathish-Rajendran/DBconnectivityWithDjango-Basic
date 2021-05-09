# Generated by Django 3.1.7 on 2021-03-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parlour_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='bill_amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bills',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bills',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_id',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_num',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='bill_amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
