from django.urls import path
from .views import GetToken, StartReg, GetCommands, GetAnswer

urlpatterns = [
    path('bot/token/', GetToken.as_view()),
    path('logging/', StartReg.as_view()),
    path('commands/', GetCommands.as_view()),
    path('content/', GetAnswer.as_view()),
]