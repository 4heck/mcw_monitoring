# Generated by Django 2.1.5 on 2019-02-17 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mon_app', '0008_auto_20190217_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='shop',
            field=models.CharField(blank=True, choices=[('M', 'Мвидео'), ('C', 'Ситилинк'), ('W', 'Wildberries')], max_length=30, null=True, verbose_name='Магазин'),
        ),
    ]