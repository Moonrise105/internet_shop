# Generated by Django 3.2.4 on 2021-06-30 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_cart_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=15, verbose_name='Сумма'),
        ),
    ]