# Generated by Django 3.1.1 on 2020-10-26 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20201026_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tranx_id',
            field=models.CharField(default='TrxID: ', max_length=50),
        ),
    ]
