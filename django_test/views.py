import form as form
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
POST_FORM = '''
<form method='post' action='/test_get_post'>
    用户名：<input type='text' name='username'>
    <input type='submit' value='提交'>
</form>
'''


def index_view(request):
    html = '<h1>Test!</h1>'
    return HttpResponse(html)


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


def test_html(request):
    dic = {
        'username':'xiaoming',
        'age':'18',
    }
    return render(request, 'test_html.html', dic)

