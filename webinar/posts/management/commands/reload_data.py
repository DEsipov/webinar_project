#!-*-coding:utf-8-*-
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from posts.models import Post, Group

User = get_user_model()


class Command(BaseCommand):
    help = 'Reload Data'
    CLASSES = (Group, Post, User)

    def erase(self):
        """Очищаем данные."""
        for cls in self.CLASSES:
            cls.objects.all().delete()

    def handle(self, *args, **options):
        self.erase()

        user = User.objects.create_superuser('vi', 'v@v.ru>', '111')
        group = Group.objects.create(title='group_one', slug='group_one', description='bada-bada')
        post = Post.objects.create(text='some text', author=user, group=group)

        print(f'Success! user: {user}, post: {post}, group: {group}')
