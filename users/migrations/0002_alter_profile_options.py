# Generated by Django 4.2.1 on 2023-06-18 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['id'], 'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
    ]