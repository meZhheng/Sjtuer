from django.contrib import admin
from .models import Book


class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'info']
    # 显示的列
    list_display_links = ['title']
    # 指定超链接位置
    list_filter = ['id']
    # 过滤器分类
    search_fields = ['title']
    # 设置模糊查询
    list_editable = ['info']
    # 设置可编辑的列,应与list_display_links互斥


admin.site.register(Book, BookManager)
