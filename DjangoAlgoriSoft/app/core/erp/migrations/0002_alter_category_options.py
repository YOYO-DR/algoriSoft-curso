# Generated by Django 4.1.7 on 2023-03-03 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Categorias', 'verbose_name_plural': 'Categorias'},
        ),
    ]
