from unicodedata import name
from django.urls import path
from .import views


urlpatterns= [
    path('',views.index,name='home'),
    path('add/',views.addphoto,name='add-photo'),
    path('about/',views.about,name='about'),
    path('add/<int:pk>/',views.photodetail.as_view(),name='view-photo'),
    path('del/<int:pk>/',views.delete,name='del-photo'),
]
