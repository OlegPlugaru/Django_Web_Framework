# Generated by Django 4.1.7 on 2023-03-07 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
