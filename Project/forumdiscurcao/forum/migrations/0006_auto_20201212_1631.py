# Generated by Django 3.1.4 on 2020-12-12 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20201212_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_post',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
