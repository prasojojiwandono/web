# Generated by Django 2.2.4 on 2019-08-05 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NamaProduct', models.CharField(max_length=255)),
                ('DeskripsiProduct', models.CharField(blank=True, max_length=255)),
                ('Tipe', models.CharField(choices=[('A', 'Tipe A'), ('B', 'Tipe B'), ('C', 'Tipe C')], max_length=10)),
            ],
        ),
    ]
