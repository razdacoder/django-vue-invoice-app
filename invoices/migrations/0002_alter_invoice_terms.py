# Generated by Django 3.2.6 on 2021-10-14 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='terms',
            field=models.CharField(choices=[('30', '30 days'), ('60', '60 days')], default=('60', '60 days'), max_length=50),
        ),
    ]
