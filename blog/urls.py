from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # post/<int:pk>/ : URL 패턴을 의미
    # post/ : URL이 post문자를 포함해야 한다
    # <int:pk> : pk라는 변수로 뷰로 전송    
    path('post/new', views.post_new, name='post_new'), 
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]