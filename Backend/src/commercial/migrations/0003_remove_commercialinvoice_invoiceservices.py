# Generated by Django 3.0.3 on 2020-05-14 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0002_commercialinvoice_invoiceservices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commercialinvoice',
            name='invoiceservices',
        ),
    ]