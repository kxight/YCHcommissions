# Generated by Django 3.1 on 2022-08-29 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20220829_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variationvalue',
            name='attachment',
            field=models.ImageField(blank=True, upload_to='photos/variations'),
        ),
    ]