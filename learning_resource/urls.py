from django.urls import path
from . import views

urlpatterns = [
    path('article_list',views.res_article_list),
    path('article/<int:res_article_id>/',views.res_article_show),
]
