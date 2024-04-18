# Generated by Django 5.0.3 on 2024-04-18 03:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.IntegerField(choices=[(1, 'By cash'), (2, 'By card'), (3, 'By balance'), (4, 'By Paypal')], verbose_name='Payment method')),
                ('payment_amount', models.IntegerField(default=0, verbose_name='Payment amount')),
                ('payment_date', models.DateTimeField(blank=True, null=True, verbose_name='Payment date')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Order is paid')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment_info', to='orders.order', verbose_name='Order')),
                ('shipping_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.usershippinginfo', verbose_name='User shipping info')),
            ],
            options={
                'verbose_name': 'payment info',
                'verbose_name_plural': 'Payment infos',
            },
        ),
    ]
