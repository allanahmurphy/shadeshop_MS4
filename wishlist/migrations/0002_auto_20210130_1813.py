# Generated by Django 3.1.5 on 2021-01-30 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='item_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='profiles.userprofile'),
        ),
    ]
