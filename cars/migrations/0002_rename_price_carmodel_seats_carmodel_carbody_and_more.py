# Generated by Django 5.0.4 on 2024-05-02 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='price',
            new_name='seats',
        ),
        migrations.AddField(
            model_name='carmodel',
            name='carBody',
            field=models.CharField(default='sedan', max_length=25),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='engine',
            field=models.FloatField(default=1.5),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.CharField(max_length=25),
        ),
    ]
