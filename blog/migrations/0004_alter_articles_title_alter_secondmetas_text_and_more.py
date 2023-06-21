# Generated by Django 4.2.1 on 2023-06-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_articles_modify_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=80, unique=True, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='secondmetas',
            name='text',
            field=models.CharField(max_length=20, unique=True, verbose_name='分类名称'),
        ),
        migrations.AlterField(
            model_name='topmetas',
            name='text',
            field=models.CharField(max_length=20, unique=True, verbose_name='分类名称'),
        ),
    ]
