import requests
from django.utils import timezone
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from news.models import News, Category, Tag


# Create your views here.

def header_component(request):
    """
    Header component view.
    """
    latest_categories = Category.objects.filter(is_active=True).order_by('-id')[:7]
    live_date = timezone.now()

    context = {
        'latest_categories': latest_categories,
        'live_date': live_date,
    }
    return render(request, 'news/base/header_component.html', context)


def footer_component(request):
    """
    Footer component view.
    """
    return render(request, 'news/base/footer_component.html')


def aside_component(request):
    """
    Main aside component view.
    """
    latest_news = News.objects.filter(is_active=True).order_by('-id')[:7]
    context = {
        'latest_news': latest_news
    }
    return render(request, 'news/base/aside_component.html', context)


def home(request):
    """
    Home view.
    """
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
    """
    The view return news by category.
    """

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
    """
    The view return news by tag.
    """

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
    """
    The view return news queries.
    """

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return News.objects.search(query)
        else:
            raise Http404

    template_name = 'news/news_list.html'


class NewsDetailView(DetailView):
    """
    The view return active news details.
    """

    def get_object(self, queryset=None):
        news_pk = self.kwargs.get('pk')
        news_slug = self.kwargs.get('slug')
        news = get_object_or_404(News, pk=news_pk, slug=news_slug)

        ip_address = self.request.user.ip_address
        if ip_address not in news.hits.all():
            news.hits.add(ip_address)

        return news

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        # related news
        first_categories = self.object.categories.first()
        context['related_news'] = News.objects.related_news(first_categories.name)
        return context

    template_name = 'news/news_detail.html'
