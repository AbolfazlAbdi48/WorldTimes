# Generated by Django 4.0 on 2021-12-18 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_ipaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='hits',
            field=models.ManyToManyField(to='news.IPAddress', verbose_name='IP Addresses'),
        ),
    ]
