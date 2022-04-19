from itertools import chain

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Note
from django.db.models import *
import random


def article_view(request):
    result = Note.objects.aggregate(total=Count('id'))
    article_id_list = random.sample(range(1, result['total']), 6)
    delicacy_list = Note.objects.filter(id__in=article_id_list)
    return render(request, 'article.html', locals())


def article_part_view(request, part):
    if part not in ['delicacy', 'traffic', 'campus', 'knowledge']:
        return HttpResponse('')
    else:
        content = Note.objects.filter(part='part')
        return render(request, 'article_part.html', locals())


def article_add_view(request):
    if request.method == "GET":
        return render(request, "article_add.html")
    elif request.method == "POST":
        title = request.POST.get("title")
        text = request.POST.get("text")
        userid = request.user.id
        Note.objects.create(title=title, content=text, user_id=userid)
        return render(request, "article_add.html")
