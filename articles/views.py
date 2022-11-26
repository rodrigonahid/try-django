from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import ArticleForm

from .models import Article

def article_view(request):
    query_dict = request.GET # this is a dictionary
    # query = query_dict.get("q") # <input type='text' name='q' />
    try:
        query = query_dict.get("q")
    except:
        query = None
    article_obj = None
    print(query)
    if query is not None:
        qs = Article.objects.search(query)
        context = {
            "object": qs
        }
        return render(request, "articles/main.html", context=context)

    if query is None:
        article_obj = Article.objects.all()
        context = {
            "object": article_obj
        }
        return render(request, "articles/main.html", context=context)
        
def article_details_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
            print(article_obj)
        except Article.MultipleObjectsReturned:
            article_obj = Article.object.filter(slug=slug).first()
        except:
            raise Http404

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