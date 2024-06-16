from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .views import preview_comment

urlpatterns = [
    path('', views.comment_list, name='comment_list'),
    path('add/', views.add_comment, name='add_comment'),
    path('captcha/', include('captcha.urls')),
    path('preview/', preview_comment, name='preview_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
