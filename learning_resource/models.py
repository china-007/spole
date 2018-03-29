from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField#引入 ckeditor 的特有类型

# Create your models here.

'''第一组'''
# 创建ResArticle 对象

class ResArticle(models.Model):
    title = models.CharField(max_length=300,verbose_name='文本标题')
    #content = models.TextField(verbose_name='文本内容')
    content = RichTextField(verbose_name='文本内容')#引入 ckeditor 编辑器
    '''字段author 规定了图片资源和用户之间的关系，一个用户对应多个资源
    使用ResPicture.author 可以查询到创建这个资源的user
    related_name="res_pictures"的作用是，
    允许使用user.res_pictures 反向查询到这个用户创建的所有图片资源
    on_delete=models.CASCADE 指的是级联删除，
    也就是主表User 中某个用户被删除的时候，他创建的资源也会自动删除'''
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="res_articles",default=None,verbose_name='创建者')
    '''自动获取当前时间'''
    created = models.DateTimeField(auto_now_add=True)#日期时间型字段
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = '文本资源'#定义对象的中文别名，用于admin 显示