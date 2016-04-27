from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic.detail import DetailView
import json


from .models import Article


class HomePageView(TemplateView):
    template_name = "articles/article_list.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['page_title'] = "Article list"
        return context


def ajax_view(request):
    total = 5
    offset = request.GET.get('offset', 0)
    end = offset + total
    print end
    if request.method == 'GET' and request.is_ajax():
        articles = Article.objects.filter(
            is_published=True).values('title', 'image', 'text', 'pk')[0:end]
        return HttpResponse(json.dumps(list(articles)), content_type='application/json')


class PostDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['page_title'] = "Article detail"
        return context
