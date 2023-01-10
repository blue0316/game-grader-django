from django.urls import path, include
from core.views import SignupView, LoginView, InviteTeamView

urlpatterns = [
    path('', LoginView.as_view(),),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('inviteteam/', InviteTeamView.as_view(), name='invite_team'),

]