# Generated by Django 4.2.2 on 2023-06-09 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tindahan', '0008_alter_orders_custname'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='hist_pic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tindahan.products'),
            preserve_default=False,
        ),
    ]
