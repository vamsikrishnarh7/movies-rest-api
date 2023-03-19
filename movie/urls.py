from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('',views.getMovie),
    path('post/', views.postMovie),
]
