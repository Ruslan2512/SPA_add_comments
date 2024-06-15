from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.comment_list, name='comment_list'),
    path('add/', views.add_comment, name='add_comment'),
    path('captcha/', include('captcha.urls')),
]
