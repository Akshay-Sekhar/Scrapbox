# Generated by Django 4.2.6 on 2024-01-20 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapboxapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('brand', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, null=True)),
                ('year', models.DateField(null=True)),
                ('picture', models.ImageField(null=True, upload_to='images')),
            ],
        ),
    ]