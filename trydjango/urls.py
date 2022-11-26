from django.contrib import admin
from django.urls import path
from articles.views import (
    article_view,
    article_details_view,
    article_create_view,
)
from accounts.views import (
    login_view,
    logout_view,
    register_view,
)
from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('articles/', article_view),
    path('articles/<slug:slug>', article_details_view),
    path('articles/create/', article_create_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
]
