from django.contrib import admin
from .models import Category, Tag, News, IPAddress


# Register your models here.
class TagInline(admin.TabularInline):
    model = News.tags.through


class CategoryInline(admin.TabularInline):
    model = News.categories.through


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
    list_filter = ('is_active', 'created', 'updated')
    list_display = ('__str__', 'is_active', 'slug', 'created', 'updated')
    list_editable = ('is_active',)


admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
    ]
    list_filter = ('is_active', 'created', 'updated')
    list_display = ('__str__', 'is_active', 'slug', 'created', 'updated')
    list_editable = ('is_active',)


admin.site.register(Tag, TagAdmin)


class NewsAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
        TagInline,
    ]
    exclude = ('categories', 'tags')
    list_filter = ('is_active', 'created', 'updated')
    list_display = ('__str__', 'thumbnail_tag', 'slug', 'is_active', 'created', 'updated')
    list_editable = ('is_active',)
    search_fields = ('title', 'description')


admin.site.register(News, NewsAdmin)
admin.site.register(IPAddress)
