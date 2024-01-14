from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView, AboutView, TerapeutasListView, TerapiasListView, RegisterView, ProfileView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('terapias/', TerapiasListView.as_view(), name='terapias'),
    path('terapeutas/', TerapeutasListView.as_view(), name='terapeutas'),
    path('profile/', login_required(ProfileView.as_view()), name='profile'),

    path('register', RegisterView.as_view(), name='register'),
]
