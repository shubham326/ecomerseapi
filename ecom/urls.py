from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', productAPI.as_view()),
    path('product/<int:pk>/', productAPI.as_view()),
]
