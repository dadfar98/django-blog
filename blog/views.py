from django.views import generic
from .models import Post


class PostHome(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-id')[:5]
    template_name = 'blog.html'

    def get_context_data(self, *args, **kwargs):
        context = super(generic.ListView, self).get_context_data(*args, **kwargs)
        context['recent_posts'] = Post.objects.all().order_by('-id')[:5]
        return context


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog_all.html'
    paginate_by = 10


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        context['recent_posts'] = Post.objects.all().order_by('-id')[:5]
        return context
