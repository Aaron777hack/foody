# Generated by Django 4.2.5 on 2023-10-04 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='views',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='file',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(),
        ),
    ]
