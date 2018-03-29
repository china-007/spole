from django.shortcuts import render
from .models import ResArticle #第1 组

# Create your views here.

def res_article_list(request):
    #通过ResArticle 对象，从数据库中读取所有的文章
    articles = ResArticle.objects.all()
    #将数据articles 渲染到模板文件article_list.html，生成网页返回给用户
    return render(request, "res_article_list.html",{"articles":articles})

#根据id，查询特定文章对象
def res_article_show(request,res_article_id):
    article = ResArticle.objects.get(id=res_article_id)
    return render(request, "res_article_content.html",{"article":article})
