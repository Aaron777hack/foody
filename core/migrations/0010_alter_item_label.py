# Generated by Django 4.2.5 on 2023-10-04 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_badge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('S', 'Start'), ('C', 'Collector'), ('P', 'Pionneer')], max_length=2),
        ),
    ]
