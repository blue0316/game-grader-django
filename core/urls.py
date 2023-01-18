from django.urls import path, include
from core.views import SignupView, LoginView, InviteTeamView, DashboardView, ProfileView, ManageTeamView, AddgameView, log_out

urlpatterns = [
    path('', LoginView.as_view(),),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('inviteteam/', InviteTeamView.as_view(), name='invite_team'),
    path('manageteam/', ManageTeamView.as_view(), name='manage_team'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('addgame/', AddgameView.as_view(), name='addgame'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', log_out, name='logout'),
]