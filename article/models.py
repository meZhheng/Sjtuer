from django.db import models
from user.models import UserInfo


class Note(models.Model):
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return '%s--%s--%s--%s' %(self.title, self.content, self.created_time, self.user_id)