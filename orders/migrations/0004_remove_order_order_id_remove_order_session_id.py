# Generated by Django 5.0.3 on 2024-04-26 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='session_id',
        ),
    ]
