from django.urls import path

from authapp.views import LoginListView, RegisterListView, Logout, profile

app_name = 'authapp'

urlpatterns = [
    path('login/', LoginListView.as_view(), name='login'),
    path('register/', RegisterListView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', Logout.as_view(), name='logout'),
]
