# Generated by Django 2.0.7 on 2018-09-04 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crcapp', '0002_auto_20180731_1343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name_plural': 'Orders'},
        ),
        migrations.RemoveField(
            model_name='car',
            name='id',
        ),
        migrations.AlterField(
            model_name='car',
            name='Car_ID',
            field=models.CharField(blank=True, max_length=10, primary_key=True, serialize=False),
        ),
    ]
