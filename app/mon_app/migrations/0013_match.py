# Generated by Django 2.1.5 on 2019-02-18 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mon_app', '0012_auto_20190218_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_product', models.IntegerField(blank=True, null=True, verbose_name='Артикул')),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Имя')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена')),
                ('status', models.BooleanField(default=True, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'сравнение',
                'verbose_name_plural': 'сравнения',
            },
        ),
    ]
