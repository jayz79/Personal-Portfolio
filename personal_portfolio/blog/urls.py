from django.urls import path, include
from . import views
from django.conf import *

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

