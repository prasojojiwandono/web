# Generated by Django 2.2.4 on 2019-08-07 05:46

from django.db import migrations, models
import produk.validators


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0002_auto_20190806_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produk',
            name='NamaProduct',
            field=models.CharField(max_length=255, validators=[produk.validators.ValidNamaProduk]),
        ),
    ]
