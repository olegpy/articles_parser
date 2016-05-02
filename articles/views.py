from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.decorators.csrf import csrf_exempt
import json


from .models import Article


class HomePageView(TemplateView):
    template_name = "articles/article_list.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['page_title'] = "Article list"
        return context


@csrf_exempt
def ajax_view(request):
    end = 5
    if request.method == 'POST' and request.is_ajax():
        end = request.POST.get('count', 0)
        return ajax_response(end)

    if request.method == 'GET' and request.is_ajax():
        return ajax_response(end)


def ajax_response(end):
    articles = Article.objects.filter(
        is_published=True).values('title', 'image', 'text', 'pk')[:end]
    return HttpResponse(json.dumps(list(articles)),
                        content_type='application/json')


class PostDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['page_title'] = "Article detail"
        return context
