# Generated by Django 4.2.2 on 2023-06-08 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tindahan', '0006_alter_orders_custname'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
