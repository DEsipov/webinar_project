from django.test import TestCase, Client
from django.urls import reverse

from posts.models import User, Post, Group


class PostCBVTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_superuser('vi', 'v@v.ru', '111')
        cls.group = Group.objects.create(title='group_one', slug='group_one', description='bada-bada')

        cls.client = Client()

        cls.form_data = {
            'text': 'About new post',
            'group': cls.group.id,
        }

    def setUp(self):
        self.client.force_login(self.user)

    def _create_post(self, text=None, group=None, author=None):
        text = text or self.form_data['text']
        group = group or self.group
        author = author or self.user
        return Post.objects.create(text=text, author=author, group=group)

    def test_index(self):
        post = self._create_post()
        url = reverse('posts:index_cbv')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.text)

    def test_post_detail(self):
        post = self._create_post()
        url = reverse('posts:post_detail_cbv', kwargs={'post_id': post.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.text)

    def test_create_post(self):
        url = reverse('posts:post_create_cbv')
        before = Post.objects.count()

        response = self.client.post(url, data=self.form_data)

        self.assertEqual(response.status_code, 302)
        after = Post.objects.count()
        self.assertEqual(after - before, 1)

    def test_edit_post(self):
        post = self._create_post()
        url = reverse('posts:post_edit_cbv', kwargs={'post_id': post.pk})
        new_text = 'new_text'

        response = self.client.post(url, data={'text': new_text})

        self.assertEqual(response.status_code, 302)
        post.refresh_from_db()
        self.assertEqual(post.text, new_text)

    def test_delete_post(self):
        post = self._create_post()
        url = reverse('posts:post_delete_cbv', kwargs={'post_id': post.pk})
        before = Post.objects.count()

        response = self.client.post(url, data=self.form_data)

        self.assertEqual(response.status_code, 302)
        after = Post.objects.count()
        self.assertEqual(before - after, 1)

    def test_reverse(self):
        post = self._create_post()

        url_index_cbv = reverse('posts:index_cbv')
        print(url_index_cbv)

        url_post_detail_cbv = reverse('posts:post_detail_cbv', kwargs={'post_id': post.pk})
        print(url_post_detail_cbv)

        url_create_post_cbv = reverse('posts:post_create_cbv')
        print(url_create_post_cbv)

        url_post_edit_cbv = reverse('posts:post_edit_cbv', kwargs={'post_id': post.pk})
        print(url_post_edit_cbv)

        url_post_delete_cbv = reverse('posts:post_delete_cbv', kwargs={'post_id': post.pk})
        print(url_post_delete_cbv)
