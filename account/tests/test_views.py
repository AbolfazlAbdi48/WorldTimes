from django.test import TestCase, Client
from django.urls import reverse

from account.models import User


class TestAccountViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.user_1 = User.objects.create(username='user_1')
        self.user_1.set_password('12345')

    def test_account_detail_user_logged_out(self):
        response = self.client.get(reverse('account:home'))

        self.assertEquals(response.status_code, 302)

    def test_account_update_post(self):
        self.client.login(username='user_1', password='12345')
        response = self.client.post(reverse('account:update'))

        self.assertEquals(response.status_code, 302)
