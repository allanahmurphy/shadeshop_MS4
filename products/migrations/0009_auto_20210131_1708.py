# Generated by Django 3.1.5 on 2021-01-31 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210131_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_credit',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='product',
            name='saleprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=254),
        ),
    ]
