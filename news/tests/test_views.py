from django.test import TestCase, Client
from django.urls import reverse
from account.models import User
from news.models import Category, Tag, News


class TestNewsViews(TestCase):

    def setUp(self):
        """
        Set up non-modified objects used by all test methods.
        """

        self.client = Client()

        # create user
        self.user_1 = User.objects.create(username='user_1')
        self.user_1.set_password('12345')

        # create category and tag
        self.category_1 = Category.objects.create(name='category 1')
        self.tag_1 = Tag.objects.create(name='tag 1')

        # create news
        self.news_1 = News.objects.create(
            title='News 1',
            description='news 1 description',
            author=self.user_1,
            image='https://cdn.pixabay.com/photo/2015/12/01/20/28/road-1072821__340.jpg'
        )
        self.news_1.categories.add(self.category_1)
        self.news_1.tags.add(self.tag_1)

        # set urls
        self.news_by_category_url = reverse('news:news-by-category', kwargs={'slug': self.category_1.slug})
        self.news_by_tag_url = reverse('news:news-by-tag', kwargs={'slug': self.tag_1.slug})
        self.news_detail_url = reverse('news:news-detail', kwargs={'pk': self.news_1.pk, 'slug': self.news_1.slug})
        self.news_search_url = f"{reverse('news:search')}?query=News 1"

    def test_news_by_category_list(self):
        """
        Test NewsByCategoryListView,
        status code,
        template used.
        """
        response = self.client.get(self.news_by_category_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news_list.html')

    def test_news_by_tag_list(self):
        """
        Test NewsByTagListView,
        status code,
        template used.
        """
        response = self.client.get(self.news_by_tag_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news_list.html')

    def test_news_detail(self):
        """
        Test NewsByDetailView,
        status code,
        template used.
        """
        response = self.client.get(self.news_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news_detail.html')

    def test_news_search_list(self):
        """
        Test SearchListView,
        status code,
        template used.
        """
        response = self.client.get(self.news_search_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news_list.html')
