from multiprocessing import context
from numbers import Number
from django.template.loader import render_to_string
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

from .models import Article

def article_search_view(request):
    try:
        query_dict = Number(request.GET.get("q"))
    except:
        query_dict = None

    article_obj = None
    if query_dict is not None:
        article_obj = Article.objects.get(id=query_dict)

    context = {
        object: article_obj,
    }
    return render(request, 'articles/search.html', context=context)

def article_view(request):
    articles = Article.objects.all()
    print(articles)
    context = {
       "articles": articles
    }

    return render(request, "articles/main.html", context=context)

def article_details_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)

    context = {
        "object": article_obj,
    }

    return render(request, 'articles/details.html', context=context)

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    } 
    if form.is_valid():
        article_object = form.save()
        
        context['object'] = article_object
        context['created'] = True

    return render(request, 'articles/create.html', context=context)