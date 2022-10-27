from django.urls import path
from .views import GetItem

urlpatterns = [
    path('', GetItem.as_view())
]