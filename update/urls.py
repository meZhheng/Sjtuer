from django.urls import path
from . import views

urlpatterns = [
    path('index_news', views.index_news_view)
]