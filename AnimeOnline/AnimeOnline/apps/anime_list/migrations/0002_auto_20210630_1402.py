# Generated by Django 2.2.24 on 2021-06-30 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime_comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='anime_list',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
