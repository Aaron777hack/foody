# Generated by Django 4.2.5 on 2023-10-04 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_item_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
    ]
