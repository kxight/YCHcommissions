# Generated by Django 3.1 on 2022-08-16 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20220816_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variationcategory',
            name='variation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.variation'),
        ),
    ]
