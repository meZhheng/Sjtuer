from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_view),
    path('add', views.article_add_view),  # 用户添加文章界面
    path('delete', views.article_delete_view),
    path('rewrite/<str:notetitle>/',views.article_rewrite_view),
    path('rewriteset/<str:notetitle>/',views.article_rewrite_set),
    path('search', views.article_search_view),
    path('wartch/<str:notetitle>/', views.article_wartch_view),
    path('praise/<str:notetitle>/',views.article_praise_view),
    path('comment/<str:notetitle>/',views.article_comment_view),
    path('deletecomment/<int:commentid>/',views.article_deletecomment_view),
    path('<str:part>', views.article_part_view),
]
