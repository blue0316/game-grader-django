from django.urls import path, include
from core.views import SignupView, LoginView, DashboardView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='login'),
]