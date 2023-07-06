# Generated by Django 4.1.2 on 2023-07-06 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=70)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=70)),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='venta.artista')),
            ],
        ),
    ]
