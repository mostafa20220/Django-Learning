from django.urls import path
from . import views

# app url name 
app_name = 'posts'

urlpatterns = [
    path('',views.posts_list,name='posts_list'),
    path('new/',views.post_new,name='new'),
    path('<slug:slug>/',views.post, name="post"),
]
