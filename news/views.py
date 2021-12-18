import requests
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from news.models import News, Category, Tag


# Create your views here.

def header_component(request):
    latest_categories = Category.objects.filter(is_active=True).order_by('-id')[:7]
    live_date = requests.get('http://api.codebazan.ir/time-date/?td=dateen')
    live_temp = requests.get('https://api.codebazan.ir/weather/?city=tehran')

    context = {
        'latest_categories': latest_categories,
        'live_date': live_date.text,
        'live_temp': live_temp.json()['result']
    }
    return render(request, 'news/base/header_component.html', context)


def aside_component(request):
    latest_news = News.objects.filter(is_active=True).order_by('-id')[:7]
    context = {
        'latest_news': latest_news
    }
    return render(request, 'news/base/aside_component.html', context)


def home(request):
    last_news = News.objects.filter(is_active=True).order_by('-id').first()
    latest_news = News.objects.filter(is_active=True).order_by('-id')[:3]
    categories = Category.objects.filter(is_active=True).order_by('-id')

    context = {
        'last_news': last_news,
        'latest_news': latest_news,
        'categories': categories
    }
    return render(request, 'news/home.html', context)


class NewsByCategoryListView(ListView):
    def get_queryset(self):
        global category
        category_slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=category_slug)

        return category.news_set.all()

    def get_context_data(self, **kwargs):
        context = super(NewsByCategoryListView, self).get_context_data(**kwargs)
        context['title'] = category
        return context

    template_name = 'news/news_list.html'


class NewsByTagListView(ListView):
    def get_queryset(self):
        global tag
        tag_slug = self.kwargs.get('slug')
        tag = get_object_or_404(Tag, slug=tag_slug)

        return tag.news_set.all()

    def get_context_data(self, **kwargs):
        context = super(NewsByTagListView, self).get_context_data(**kwargs)
        context['title'] = tag.name
        return context

    template_name = 'news/news_list.html'


class SearchListView(ListView):
    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return News.objects.search(query)
        else:
            raise Http404

    template_name = 'news/news_list.html'


class NewsDetailView(DetailView):
    def get_object(self, queryset=None):
        news_pk = self.kwargs.get('pk')
        news_slug = self.kwargs.get('slug')
        news = get_object_or_404(News, pk=news_pk, slug=news_slug)

        return news

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        # related news
        first_categories = self.object.categories.first()
        context['related_news'] = News.objects.related_news(first_categories.name)
        return context

    template_name = 'news/news_detail.html'
