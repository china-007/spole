from django.contrib import admin
from .models import ResArticle
# Register your models here.


admin.site.site_header = '楚雄师范学院SPOLE 课程管理系统' 
admin.site.site_title = '楚雄师院SPOLE' # 此处设置页面头部标题

admin.site.register(ResArticle)