# Generated by Django 4.2.5 on 2023-10-03 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_uploadedfile_item_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='file',
            field=models.FileField(upload_to='extracted/'),
        ),
    ]
