from django.urls import path
from mainapp.views import Index, LoginApp, RegisterApp, LogoutApp

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', LoginApp.as_view(), name='log_in'),
    path('sign_up/', RegisterApp.as_view(), name='registration'),
    path('logout/', LogoutApp.as_view(), name='log_out'),
]