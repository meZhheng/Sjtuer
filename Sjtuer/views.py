from update.models import Newslist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import login, logout, authenticate
from user.models import UserInfo
from article.models import Note

POST_FORM = '''
<form method='post' action='/test_get_post'>
    用户名：<input type='text' name='username'>
    <input type='submit' value='提交'>
</form>
'''


def user_view(request):
    return render(request, 'user/user.html')


def register_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        account = request.POST['account']
        password = request.POST['password']
        # email = request.POST['email']
        # phone = request.POST['phone']
        old_user = UserInfo.objects.filter(username=account)
        if old_user:
            return HttpResponse('---用户名已被占用---')
        try:
            user = UserInfo.objects.create_user(username=account, password=password)
        except Exception as err:
            print('--create user error %s' % err)
            return HttpResponse('--用户名已被占用---')
        login(request, user)
        return HttpResponseRedirect('index')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        account = request.POST['account']
        password = request.POST['password']
        user = authenticate(username=account, password=password)
        if not user:
            return render(request, 'user/user.html', {'login_fail': True})
        else:
            login(request, user)
            return HttpResponseRedirect('index')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('index')


def index_view(request):
    news_list = Newslist.objects.filter(title='交大要闻')
    notice_list = Newslist.objects.filter(title='通知通告')
    focus_list = Newslist.objects.filter(title='媒体聚焦')

    user = request.user
    notlogin = isinstance(user, AnonymousUser)
    return render(request, 'Sjtuer_index.html', locals())


def userspace_view(request):
    work_list = Note.objects.filter(user_id=request.user.id, isactive=True)
    return render(request, 'user/space.html', locals())


def page_invalid_view(request, pg):
    html = '<h1>这是编号为%s的页面</h1>' % pg
    return HttpResponse(html)


def page_valid_view(request, pg):
    return HttpResponse('合法输入！')


def cal1_view(request, m, op, n):
    if op not in ['add', 'sub', 'mul']:
        return HttpResponse()
    result = 0
    if op == 'add':
        result = m + n
    return HttpResponse(result)


def cal2_view(request, x, op, y):
    return HttpResponse('x:%s op:%s y:%s' % (x, op, y))


def request_study_view(request):
    # request的各种方法可以获取很多请求中的属性
    url = request.path_info
    method = request.method
    data_get = request.GET
    data_post = request.POST
    print(url + ' ' + method)
    print(data_get)
    print(request.get_full_path())
    # 打印到终端
    return HttpResponseRedirect('/page/1')


def test_getmethod(request):
    if request.method == 'GET':
        # print(request.GET)
        # print(request.GET['a'])
        # print(request.GET.getlist('a'))
        # print(request.GET.get('c', 0))
        return HttpResponse(POST_FORM)
    elif request.method == 'POST':
        uname = 'username is %s' % request.POST['username']
        return HttpResponse(uname)
    else:
        pass
    return HttpResponse('successfully get post')
