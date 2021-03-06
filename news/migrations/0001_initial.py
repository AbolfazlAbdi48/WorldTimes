# Generated by Django 4.0 on 2021-12-17 17:52

from django.db import migrations, models
import django.db.models.deletion
import news.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Category Name')),
                ('slug', models.SlugField(blank=True, verbose_name='Category Slug')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active/DeActive')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Tag Name')),
                ('slug', models.SlugField(blank=True, verbose_name='Tag Slug')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active/DeActive')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, verbose_name='News Slug')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to=news.models.upload_image_path, verbose_name='image')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active/DeActive')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='account.user', verbose_name='Author')),
                ('categories', models.ManyToManyField(to='news.Category', verbose_name='Categories')),
                ('tags', models.ManyToManyField(to='news.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
    ]
