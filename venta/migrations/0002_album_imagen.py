# Generated by Django 4.1.2 on 2023-07-06 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='imagen',
            field=models.ImageField(null=True, upload_to='albums'),
        ),
    ]
