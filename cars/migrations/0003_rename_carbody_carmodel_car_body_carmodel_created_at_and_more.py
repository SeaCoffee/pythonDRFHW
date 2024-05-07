# Generated by Django 5.0.4 on 2024-05-02 08:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rename_price_carmodel_seats_carmodel_carbody_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='carBody',
            new_name='car_body',
        ),
        migrations.AddField(
            model_name='carmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
