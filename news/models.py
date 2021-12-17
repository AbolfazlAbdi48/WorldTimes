import os
from random import randint
from django.utils import timezone
from django.db import models
from django.template.defaultfilters import slugify
from account.models import User
from django.utils.html import format_html


# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    number_random_1 = randint(2000, 10000)
    now_time = timezone.now()
    final_name = f"{number_random_1}-news-image-{now_time}{ext}"
    return f"articles/{final_name}"


class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name='Category Name')
    slug = models.SlugField(blank=True, verbose_name='Category Slug')
    is_active = models.BooleanField(default=True, verbose_name='Active/DeActive')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class Tag(models.Model):
    name = models.CharField(max_length=120, verbose_name='Tag Name')
    slug = models.SlugField(blank=True, verbose_name='Tag Slug')
    is_active = models.BooleanField(default=True, verbose_name='Active/DeActive')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class News(models.Model):
    title = models.CharField(max_length=120, verbose_name='Title')
    slug = models.SlugField(blank=True, verbose_name='News Slug')
    description = models.TextField(verbose_name='Description')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Author', related_name='news'
    )
    image = models.ImageField(
        upload_to=upload_image_path, verbose_name='image'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='Active/DeActive'
    )
    categories = models.ManyToManyField(Category, verbose_name='Categories')
    tags = models.ManyToManyField(Tag, verbose_name='Tags')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def thumbnail_tag(self):
        return format_html(f"<img width=100 height=75 style='border-radius: 5px;' src='{self.image.url}'>")

    thumbnail_tag.short_description = "Thumbnail"

    def __str__(self):
        return f'{self.title}'
