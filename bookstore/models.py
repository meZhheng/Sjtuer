from django.db import models


# python manage.py makemigrations
# python manage.py migrate

# python manage.py shell

# myModel.objects.create(column1 = value1, ...)
# myModel.objects.all() 返回QuerySet
# myModel.objects.get(条件1， 条件2， ...) 返回唯一数据，数据多于1条或没有数据均报错
# myModel.objects.filter(条件1， 条件2， ...) 返回QuerySet
# myModel.objects.exclude(条件1， 条件2， ...) 返回QuerySet
# myModel.objects.value(column1, column2, ...) 返回字典
# myModel.objects.value_list(column1, column2, ...) 返回元组
# myModel.objects.order_by(column1, -column2, ...) 返回QuerySet
# QuerySet类型可作进一步查询,多个查询顺序可变,django自动转换
# myQuerySet.query 返回sql语句

# 非等值查询：查询谓词
# __exact 等值查询 =, is
# __contains 包含指定值 like
# __startwith
# __endwith
# __gt 大于
# __gte 大于等于
# __lt
# __lte
# __in __in['', '', '', ...]
# __range __range(a,b)

'''
    更改单条数据
        1.查询得到该数据对应的object，使用get()方法
        2.修改对应列 objects.column = xxx
        3.保存 object.save()
    批量数据更新
        1.查询得到对应的QuerySet，使用filter()，all()方法
        2.使用queryset.update(column=value),更新数据
'''

'''
    删除单条数据
        1.查询 get()
        2.objects.delete()
    删除批量数据
        1.查询 filter(),all()
        2.objects.delete()
'''


class Book(models.Model):

    title = models.CharField('title', max_length=50, default='')
    price = models.DecimalField('price', max_digits=7, decimal_places=2, default=0.0)
    info = models.CharField('描述', max_length=100, default='')
    is_active = models.BooleanField('是否活跃', default=True)

    class Meta:
        # Meta类用于修改模型类（表）本身的属性
        db_table = 'book'

    def _str_(self):

        return '%s_%s_%s' % (self.title, self.price, self.info)


class Author(models.Model):

    name = models.CharField('姓名', max_length=11)
    age = models.IntegerField('年龄')
    email = models.EmailField('邮箱')
