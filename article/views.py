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
        module = request.POST.get("module")
        userid = request.user.id
        Note.objects.create(title=title, content=text, module=module, user_id=userid)
        return render(request, "article_add.html")


def article_search_view(request):
    # data=json.loads(request.body)
    # q=data.get('q')
    if request.method == "GET":
        return render(request, "article.html")
    elif request.method == "POST":
        # data = json.loads(request.body)
        # content=data.get('content')
        content = request.POST.get("content")  # 要与html中的名字一致妈了比比
        notetitle_list = Note.objects.filter(Q(content__icontains=content) | Q(title__icontains=content)
                                             | Q(user__username__icontains=content))
        return render(request, "results.html", {'notetitle_list': notetitle_list})


def article_wartch_view(request, notetitle):
    try:
        note = Note.objects.get(title=notetitle)
    except Exception as err:
        return HttpResponse('The note is not existed %s' % err)
    return render(request, 'watch.html', {'note': note})
