# Generated by Django 5.1.3 on 2024-11-19 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm_app', '0002_product_pimage_alter_product_cat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.ForeignKey(db_column='pid', on_delete=django.db.models.deletion.CASCADE, to='ecomm_app.product')),
            ],
        ),
    ]
