from itertools import chain

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from user.models import UserInfo
from .models import Note
from django.db.models import *
import random
from .models import praising,comment


def article_view(request):
    result = Note.objects.aggregate(total=Count('id'))
    article_id_list = random.sample(range(1, result['total']), 3)
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


def article_delete_view(request):
    if request.method == "GET":
        return render(request, "article.html")
    elif request.method == "POST":
        print(request.GET.get("id"))
        try:
            article = Note.objects.get(id=request.GET.get("id"))
            article.isactive = False
            article.save()
        except Exception as err:
            print('---delete article error as %s' % err)
            return HttpResponseRedirect('/space')
    return HttpResponseRedirect('/space')


def article_search_view(request):
    # data=json.loads(request.body)
    # q=data.get('q')
    if request.method == "GET":
        return render(request, "article.html")
    elif request.method == "POST":
        # data = json.loads(request.body)
        # content=data.get('content')
        content = request.POST.get("content")
        title_list = Note.objects.filter(title__icontains=content)
        content_list = Note.objects.filter(content__icontains=content)
        user_list = Note.objects.filter (user__username__icontains=content)
        all_set=set(title_list)&set(user_list)&set(content_list)
        tc_set=(set(title_list)&set(content_list))-all_set
        tu_set=(set(title_list)&set(user_list))-all_set
        cu_set=(set(content_list)&set(user_list))-all_set
        ot_set=set(title_list)-set(user_list)-set(content_list)
        oc_set=set(content_list)-set(user_list)-set(title_list)
        ou_set=set(user_list)-set(content_list)-set(title_list)
        all_list=list(all_set)
        tc_list=list(tc_set)
        tu_list=list(tu_set)
        cu_list=list(cu_set)
        ot_list = list (ot_set)
        oc_list = list (oc_set)
        ou_list=list(ou_set)
        return render(request, "results.html", {'content':content,'all':all_list,'tc':tc_list,'tu':tu_list,'cu':cu_list,'ot':ot_list,'oc':oc_list,'ou':ou_list})


def article_wartch_view(request, notetitle):
    user=request.user
    try:
        note = Note.objects.get(title=notetitle)
    except Exception as err:
        return HttpResponse('The note is not existed ' )
    temp=Note.objects.get(title=notetitle)
    praisinglist = praising.objects.filter (article=temp)
    praiserlist = []
    for praisingsample in praisinglist:
        thepraiser = UserInfo.objects.get (id=praisingsample.praiserid)
        praisername = thepraiser.username
        if praisername not in praiserlist:
            praiserlist.append (praisername)
    commenting=comment.objects.filter(article=temp)
    if user.username not in praiserlist:
        yes=1
    else:
        yes=0
    return render(request, 'watch.html', {'note': note,'prase':praiserlist,'commenting':commenting,'user':user,'yes':yes})

def article_rewrite_view(request,notetitle):
    try:
        note = Note.objects.get(title=notetitle)
    except Exception as err:
        return HttpResponse('The note is not existed ' )
    return render(request,'rewrite.html',{'note':note})

def article_rewrite_set(request,notetitle):
    try:
        note = Note.objects.get(title=notetitle)
    except Exception as err:
        return HttpResponse('The note is not existed ' )
    if request.method == 'GET':
        return render (request, '/login.html')
    elif request.method == 'POST':
        note.title = request.POST.get('title',"")
        note.content = request.POST.get('content',"")
        note.save()
        return HttpResponseRedirect ('/space')
        return render (request,'/space')


def article_praise_view(request,notetitle):
    if request.method == 'GET':
        return render (request, '/login.html')
    elif request.method == 'POST':
        temp=Note.objects.get(title=notetitle)
        praisinglist=praising.objects.filter(article=temp)
        praiserlist=[]
        for praisingsample in praisinglist:
            thepraiser=UserInfo.objects.get(id=praisingsample.praiserid)
            praisername=thepraiser.username
            if praisername not in praiserlist:
                praiserlist.append(praisername)
        praiser = request.user
        praisername1=praiser.username
        if praisername1 not in praiserlist:
            writer=temp.user
            praising.objects.create(article=temp,praiserid=praiser.id,writer=writer)


        else:
            temppraise=praising.objects.get(praiserid=praiser.id,article=temp)
            temppraise.delete()

        commenting = comment.objects.filter (article=temp)
        praisinglist = praising.objects.filter (article=temp)
        praiserlist = []

        for praisingsample in praisinglist:
            thepraiser = UserInfo.objects.get (id=praisingsample.praiserid)
            praisername = thepraiser.username
            if praisername not in praiserlist:
                praiserlist.append (praisername)
        if praisername1 not in praiserlist:
            yes=1
        else:
            yes=0
        return render(request, 'watch.html', {'note': temp,'prase':praiserlist,'commenting':commenting,'user':praiser,'yes':yes})

def article_comment_view(request,notetitle):
     if request.method == 'GET':
        return render (request, '/login.html')
     elif request.method == 'POST':
        tempuser=request.user
        temparticle=Note.objects.get(title=notetitle)
        tempcomment=request.POST.get("comment")
        comment.objects.create(commentator=tempuser,article=temparticle,commentchar=tempcomment)
        commenting = comment.objects.filter (article=temparticle)
        praisinglist = praising.objects.filter (article=temparticle)
        praiserlist = []
        for praisingsample in praisinglist:
            thepraiser = UserInfo.objects.get (id=praisingsample.praiserid)
            praisername = thepraiser.username
            if praisername not in praiserlist:
                praiserlist.append (praisername)
        if tempuser.username not in praiserlist:
            yes=1
        else:
            yes=0
        return render (request, 'watch.html', {'note': temparticle, 'prase': praiserlist, 'commenting': commenting,'user':tempuser,'yes':yes})

def article_deletecomment_view(request,commentid):
    tempcomment=comment.objects.get(id=commentid)
    tempuser = request.user
    temparticle=tempcomment.article
    commenting = comment.objects.filter (article=temparticle)
    praisinglist = praising.objects.filter (article=temparticle)
    praiserlist = []
    for praisingsample in praisinglist:
        thepraiser = UserInfo.objects.get (id=praisingsample.praiserid)
        praisername = thepraiser.username
        if praisername not in praiserlist:
            praiserlist.append (praisername)
    if tempuser.username not in praiserlist:
        yes = 1
    else:
        yes = 0

    tempcomment.delete()
    return render (request, 'watch.html',
                   {'note': temparticle, 'prase': praiserlist, 'commenting': commenting, 'user': tempuser,'yes':yes})