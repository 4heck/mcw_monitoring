# Generated by Django 2.1.5 on 2019-02-18 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mon_app', '0015_auto_20190218_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='match',
            name='id_product2',
        ),
        migrations.RemoveField(
            model_name='match',
            name='name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='name2',
        ),
        migrations.RemoveField(
            model_name='match',
            name='price',
        ),
        migrations.RemoveField(
            model_name='match',
            name='price2',
        ),
        migrations.AddField(
            model_name='match',
            name='id_product_conc',
            field=models.IntegerField(blank=True, null=True, verbose_name='Артикул конкурента'),
        ),
        migrations.AddField(
            model_name='match',
            name='id_product_my',
            field=models.IntegerField(blank=True, null=True, verbose_name='Артикул MyShop'),
        ),
        migrations.AddField(
            model_name='match',
            name='name_conc',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Имя конкурента'),
        ),
        migrations.AddField(
            model_name='match',
            name='name_my',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Имя MyShop'),
        ),
        migrations.AddField(
            model_name='match',
            name='price_conc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена конкурента'),
        ),
        migrations.AddField(
            model_name='match',
            name='price_my',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена MyShop'),
        ),
        migrations.AlterField(
            model_name='match',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата сравнения'),
        ),
    ]
