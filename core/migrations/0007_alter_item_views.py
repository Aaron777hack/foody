# Generated by Django 4.2.5 on 2023-10-04 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_item_views_alter_item_file_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
