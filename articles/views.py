from multiprocessing import context
from numbers import Number
from django.template.loader import render_to_string
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

from .models import Article

def article_search_view(request):
    query_dict = request.GET # this is a dictionary
    # query = query_dict.get("q") # <input type='text' name='q' />
    try:
        query = int(query_dict.get("q"))
    except:
        query = None
    article_obj = None
    print("query", query)
    if query is not None:
        article_obj = Article.objects.get(id=query)
        context = {
            "object": article_obj
        }
        return render(request, "articles/search.html", context=context)

    if query is None:
        article_obj = Article.objects.all()
        context = {
            "object": article_obj
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