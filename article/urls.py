from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_view),
    path('add', views.article_add_view),  # 用户添加文章界面
    path('search', views.article_search_view),
    path('wartch/<str:notetitle>/', views.article_wartch_view),
    path('<str:part>', views.article_part_view),
]
