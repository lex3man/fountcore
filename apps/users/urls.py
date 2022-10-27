from django.urls import path
from .views import UserAdd

urlpatterns = [
    path('new/', UserAdd.as_view()),
]