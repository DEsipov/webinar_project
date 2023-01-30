from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)

from posts.forms import PostForm
from posts.models import Post


class PostListView(ListView):
    """Отображения списка постов."""
    queryset = Post.objects.all()
    # Имя переменной в шаблоне.
    context_object_name = 'page_obj'
    # Кол-во записей на странице.
    paginate_by = 2
    template_name = 'posts/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """Добавление экста контекста."""
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = 'Hello World!'
        return context


class PostDetailView(DetailView):
    """Отображение конкретного поста."""
    # Модель, которая используется.
    model = Post
    template_name = 'posts/post_detail.html'
    # Имя параметра в url
    pk_url_kwarg = 'post_id'
    # Имя переменной в шаблоне.
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Создание поста, требующее логина (миксин)."""
    model = Post
    # Название формы, которая будет использоваться.
    form_class = PostForm
    template_name = 'posts/create_post.html'
    # Адрес, куда будет перенаправлен пользователь,
    # после успешного создания объекта.
    # Можем указать так, но если нужна более сложная логика, то переопределяем
    # метод get_success_url
    # success_url = reverse_lazy('posts:index')

    def form_valid(self, form):
        """Переопределяем логику сохранения формы."""
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        """Переопределяем редирект после создания."""
        return reverse_lazy('posts:post_detail',
                            kwargs={'post_id': self.object.id})


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Редактирование поста. Которое требует логина и разрешений."""
    model = Post
    form_class = PostForm
    template_name = 'posts/create_post.html'
    # Имя параметра в url.
    pk_url_kwarg = 'post_id'

    def has_permission(self):
        """Переопределяем логику пермишенов."""
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Редактирование поста."""
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('posts:index')

    def has_permission(self):
        """Переопределяем логику пермишенов."""
        post = self.get_object()
        return self.request.user == post.author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'В топку!'
        return context
