from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post
from .utils import paginate_page


def index(request):
    """Главная страница."""
    template = 'posts/index.html'
    posts = Post.objects.select_related('group', 'author')
    page_obj = paginate_page(request, posts)
    context = {'page_obj': page_obj}
    return render(request, template, context)


def post_detail(request, post_id):
    """Страница детального просмотра поста."""
    post = get_object_or_404(Post, id=post_id)
    template = 'posts/post_detail.html'
    context = {
        'post': post,
    }
    return render(request, template, context)


@login_required
def post_create(request):
    """Страница создания поста"""
    if request.user.is_authenticated():
        pass

    form = PostForm(request.POST or None)
    if not request.method == 'POST':
        return render(request, 'posts/create_post.html', {'form': form})

    if not form.is_valid():
        return render(request, 'posts/create_post.html', {'form': form})

    post = form.save(commit=False)
    post.author = request.user
    post.save()
    return redirect('posts:post_detail', post.id)


@login_required
def post_edit(request, post_id):
    """Страница редактирования поста."""
    template = 'posts/create_post.html'
    post = get_object_or_404(Post, id=post_id)

    if post_id and request.user != post.author:
        return redirect('posts:post_detail', post_id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post_id)

    context = {
        'form': form,
        'post': post,
        'is_edit': True,
    }
    return render(request, template, context)


@login_required
def post_delete(request, post_id):
    """Страница редактирования поста."""
    post = get_object_or_404(Post, id=post_id)
    if post_id and request.user != post.author:
        return redirect('posts:post_detail', post_id=post_id)

    post.delete()
    return redirect('posts:index', post_id=post_id)
