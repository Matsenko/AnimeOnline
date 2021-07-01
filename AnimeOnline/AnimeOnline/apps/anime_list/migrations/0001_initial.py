# Generated by Django 3.2.4 on 2021-06-11 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime_name', models.CharField(max_length=200, verbose_name='Anime name')),
                ('anime_text', models.TextField(verbose_name='Anime description')),
                ('pub_date', models.DateTimeField(verbose_name='Publication date')),
            ],
        ),
        migrations.CreateModel(
            name='Anime_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Author name')),
                ('comment_text', models.TextField(verbose_name='Comment')),
                ('pub_date', models.DateTimeField(verbose_name='Publication date')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime_list.anime_list')),
            ],
        ),
    ]
