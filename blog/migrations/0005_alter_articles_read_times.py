# Generated by Django 4.2.1 on 2023-06-18 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_articles_title_alter_secondmetas_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='read_times',
            field=models.IntegerField(default=0, editable=False, verbose_name='阅读次数'),
        ),
    ]