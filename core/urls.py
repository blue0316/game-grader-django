from django.urls import path, include
from core.views import SignupView, LoginView, InviteTeamView, DashboardView, ProfileView, ManageTeamView, AddgameView, HomeView, NewPlanView, NewEventView, log_out,MondayCorrections

urlpatterns = [
    path('', LoginView.as_view(),),
    path('signup/', SignupView.as_view(), name='signup'),
    path('home/', HomeView.as_view(), name='home'),
    path('monday/',MondayCorrections.as_view(),name="monday_corrections"),
    path('login/', LoginView.as_view(), name='login'),
    path('inviteteam/', InviteTeamView.as_view(), name='invite_team'),
    path('manageteam/', ManageTeamView.as_view(), name='manage_team'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('addgame/', AddgameView.as_view(), name='addgame'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('newplan/', NewPlanView.as_view(), name='new_plan'),
    path('newevent/', NewEventView.as_view(), name='new_event'),
    path('logout/', log_out, name='logout'),
]