from django.test import TestCase, Client
from django.urls import reverse
from .models import Comment
from .forms import CommentForm
from PIL import Image
import tempfile
import os
from django.core.files.uploadedfile import SimpleUploadedFile


class CommentTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.comment_url = reverse('comment_list')
        self.add_comment_url = reverse('add_comment')
        self.preview_comment_url = reverse('preview_comment')
        self.image = self.generate_test_image()
        self.text_file = SimpleUploadedFile("file.txt", b"file_content", content_type="text/plain")

    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 302)

    def generate_test_image(self):
        image = Image.new('RGB', (320, 240), 'white')
        temp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(temp_file)
        temp_file.seek(0)
        return SimpleUploadedFile(temp_file.name, temp_file.read(), content_type='image/jpeg')

    def test_add_comment_with_image(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'text': 'This is a test comment',
        }
        files = {
            'image': self.image
        }
        response = self.client.post(self.add_comment_url, data=form_data, files=files)
        self.assertEqual(response.status_code, 200)

    def test_add_comment_with_text_file(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'text': 'This is a test comment',
        }
        files = {
            'text_file': self.text_file
        }
        response = self.client.post(self.add_comment_url, data=form_data, files=files)
        self.assertEqual(response.status_code, 200)

    def test_preview_comment(self):
        response = self.client.post(self.preview_comment_url, {'text': '<strong>Bold text</strong>'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('<strong>Bold text</strong>', response.json()['preview'])

    def test_pagination(self):
        for i in range(30):
            Comment.objects.create(username='testuser', email='test@example.com', text=f'Test comment {i}')
        response = self.client.get(self.comment_url)
        self.assertEqual(response.status_code, 200)

    def test_comment_list_ordering(self):
        Comment.objects.create(username='testuser1', email='test1@example.com', text='First comment')
        Comment.objects.create(username='testuser2', email='test2@example.com', text='Second comment')
        response = self.client.get(self.comment_url, {'sort_by': 'username', 'order': 'asc'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'First comment')
        self.assertContains(response, 'Second comment')

    def tearDown(self):
        # Delete all created files after tests
        for comment in Comment.objects.all():
            if comment.image:
                if os.path.isfile(comment.image.path):
                    os.remove(comment.image.path)
            if comment.text_file:
                if os.path.isfile(comment.text_file.path):
                    os.remove(comment.text_file.path)
