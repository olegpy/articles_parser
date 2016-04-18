from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article


class PostListView(ListView):
    queryset = Article.objects.filter(is_published=True)
    paginate_by = 5
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['page_title'] = "Article list"
        return context


class PostDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['page_title'] = "Article detail"
        return context

# Create your views here.
