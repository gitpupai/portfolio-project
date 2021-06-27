from django.urls import path
from . import views

app_name='blog'
#here urlpatterns starts after http://127.0.0.1:8000/blog/
urlpatterns = [
    path('',views.bloghome,name='bloghomepage'), #it will go to blog's views.py
    path('<int:blog_id>/',views.details,name='detailspage'),
]
