# Generated by Django 4.2.6 on 2024-01-20 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapboxapp', '0003_product_category_product_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='year',
            field=models.TextField(null=True),
        ),
    ]