# Generated by Django 3.1 on 2020-10-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20201013_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikes',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=20, max_digits=10),
        ),
    ]