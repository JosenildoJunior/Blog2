# Generated by Django 3.1.4 on 2020-12-12 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_remove_post_resumo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]
