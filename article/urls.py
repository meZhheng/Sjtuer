from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_view),
    path('add', views.article_add_view),  # 用户添加文章界面
    path('<str:part>', views.article_part_view)
]
