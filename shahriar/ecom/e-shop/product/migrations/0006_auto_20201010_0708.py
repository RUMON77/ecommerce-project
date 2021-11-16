# Generated by Django 3.1.1 on 2020-10-10 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20201010_0700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='notes',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='011', max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='tranx_id',
            field=models.CharField(default='sfgn', max_length=50),
            preserve_default=False,
        ),
    ]
