# Generated by Django 2.1.5 on 2019-02-19 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mon_app', '0026_auto_20190219_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='url',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Ссылка'),
        ),
    ]
