# Generated by Django 3.1 on 2022-08-17 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20220817_1712'),
        ('carts', '0003_cartitem_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.VariationValue'),
        ),
    ]
