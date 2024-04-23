from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from cards.models import Card
from drf.permissions import TrelloUndercutPermissions, UsersCreateTrelloUndercutPermissions
from drf.serializers import TaskDashboardUserSerializer, CardCreateUserSerializer, \
    CardListSerializer, CardUpdateUserSerializer, CardUpdateAdminSerializer
from mainapp.constants import CardStatus
from mainapp.models import TaskDashboardUser


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardListSerializer
    permission_classes = (TrelloUndercutPermissions, )

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            if not self.request.user.is_superuser:
                self.serializer_class = CardCreateUserSerializer
        if self.action == "update":
            if self.request.user.is_superuser:
                self.serializer_class = CardUpdateAdminSerializer
            else:
                self.serializer_class = CardUpdateUserSerializer

        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)


class CardAPIList(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardListSerializer

    def get(self, request, *args, **kwargs):
        try: kwargs['status']
        except:
            return Response({'error': "Object does not exists"})
        status = CardStatus.LOWER_STATUS_DICT[kwargs['status']]
        self.queryset = Card.objects.filter(status=status)
        return self.list(request, *args, **kwargs)


class UserAPIView(generics.ListCreateAPIView):
    queryset = TaskDashboardUser.objects.all()
    serializer_class = TaskDashboardUserSerializer
    permission_classes = (AllowAny, )





