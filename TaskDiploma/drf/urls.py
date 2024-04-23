from django.urls import path, include
from rest_framework import routers
from drf.views import CardViewSet, CardAPIList, UserAPIView

router = routers.DefaultRouter()
router.register(r'cards', CardViewSet,)


urlpatterns = [
    path('', include(router.urls)),
    path('trelloundercut/auth/', include('rest_framework.urls')),
    path('cards/status/<str:status>/', CardAPIList.as_view()),
    path('user/', UserAPIView.as_view()),

]