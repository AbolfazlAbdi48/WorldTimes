from django.test import TestCase

from account.models import User
from news.models import Category, Tag, News


class TestNewsModel(TestCase):

    def setUp(self):
        """
        Set up non-modified objects used by all test methods.
        """
        
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

    def test_news_title_max_length(self):
        news = self.news_1
        max_length = news._meta.get_field('title').max_length

        self.assertEquals(max_length, 120)

    def test_news_categories_field_blank(self):
        news = self.news_1
        blank = news._meta.get_field('categories').blank

        self.assertEquals(blank, False)

    def test_news_tags_field_blank(self):
        news = self.news_1
        blank = news._meta.get_field('tags').blank

        self.assertEquals(blank, False)

    def test_news_hits_field_blank(self):
        news = self.news_1
        blank = news._meta.get_field('hits').blank

        self.assertEquals(blank, True)
