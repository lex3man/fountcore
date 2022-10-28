from django.urls import path
from .views import GetToken, StartReg, GetCommands, FindAnswer

urlpatterns = [
    path('bot/token/', GetToken.as_view()),
    path('logging/', StartReg.as_view()),
    path('commands/', GetCommands.as_view()),
    path('content/', FindAnswer.as_view()),
]
