# Generated by Django 4.1.7 on 2023-05-04 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tindahan', '0003_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='oprice',
            new_name='quantity',
        ),
    ]
