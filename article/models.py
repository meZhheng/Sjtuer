#
from django.db import models
from user.models import UserInfo


class Note(models.Model):
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容')
    module = models.CharField('模块', max_length=50, default="其他")
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    picture = models.FileField('图片', upload_to="image_upload_test")
    isactive = models.BooleanField('是否活跃', default=True)



class comment(models.Model):
    article = models.ForeignKey (Note, on_delete=models.CASCADE, default='文章')
    commentchar=models.CharField('评论内容', max_length=100,default="空")
    commentator=models.ForeignKey(UserInfo,on_delete=models.CASCADE,default='用户')


class praising(models.Model):
    writer=models.ForeignKey(UserInfo,on_delete=models.CASCADE,default='用户')
    article=models.ForeignKey(Note,on_delete=models.CASCADE,default='文章')
    praiserid=models.IntegerField(default='0')