# Generated by Django 3.1 on 2022-08-16 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_variationcategory_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variationcategory',
            name='variation',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='store.variation'),
        ),
    ]
