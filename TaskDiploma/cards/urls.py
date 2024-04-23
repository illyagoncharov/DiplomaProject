from django.urls import path
from cards.views import TaskDashboard, CardCreate, CardEdit, CardDelete

app_name = 'cards'

urlpatterns = [
    path('', TaskDashboard.as_view(), name='taskdashboard'),
    path('cardcreate', CardCreate.as_view(), name='cardcreate'),
    path('cardedit', CardEdit.as_view(), name='cardedit'),
    path('cardelete/<int:pk>/', CardDelete.as_view(), name='carddelete'),

    ]