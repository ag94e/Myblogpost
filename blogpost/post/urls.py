from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('<slug:post>/', views.single_post, name='single_post'),
]