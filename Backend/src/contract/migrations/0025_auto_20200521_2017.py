# Generated by Django 3.0.3 on 2020-05-21 20:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0024_auto_20200521_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='deadDatePay',
            field=models.DateField(default=datetime.datetime(2020, 5, 31, 20, 17, 12, 176661)),
        ),
    ]
