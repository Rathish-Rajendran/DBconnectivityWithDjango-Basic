# Generated by Django 3.1.7 on 2021-03-28 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parlour_management', '0002_auto_20210328_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='contact_num',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
