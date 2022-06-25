from django.urls import path
from . import views
# 127.0.0.1:8000
urlpatterns = [
    path('/',views.home , name = "home"),
]