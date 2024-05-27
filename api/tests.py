from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post

class PostAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_post_with_empty_fields(self):
        url = '/api/posts/'
        data = {
            'title': '',
            'username': '',
            'content': ''
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_post_with_empty_fields(self):
        post = Post.objects.create(title='Test Post', username='testuser', content='Test Content')
        url = f'/api/posts/{post.id}/'
        data = {
            'title': '',
            'username': '',
            'content': ''
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)