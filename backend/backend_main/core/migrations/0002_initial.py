# Generated by Django 5.0.3 on 2024-05-25 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='pchCustIdfk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customertable'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='pchPmtIdfk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.paymentmethod'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='pchPstIdfk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.paymentstatus'),
        ),
    ]
