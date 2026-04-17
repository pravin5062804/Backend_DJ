from django.urls import path,include
from todolist import views

urlpatterns = [
    path('',views.home,name="todolist"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('blog/',views.blog,name="blog"),
]
