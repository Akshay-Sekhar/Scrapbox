# Generated by Django 4.2.6 on 2024-01-22 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapboxapp', '0004_alter_product_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
