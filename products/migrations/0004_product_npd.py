# Generated by Django 3.2.8 on 2021-10-06 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211006_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='npd',
            field=models.DecimalField(blank=True, decimal_places=2, default=2, max_digits=10),
            preserve_default=False,
        ),
    ]
