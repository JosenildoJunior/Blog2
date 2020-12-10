# Generated by Django 3.1.4 on 2020-12-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('conteudo', models.CharField(max_length=500)),
                ('data_post', models.DateTimeField(verbose_name='Data da publicação')),
            ],
        ),
    ]