from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from cards.models import Card
from mainapp.constants import CardStatus
from mainapp.models import TaskDashboardUser


class CardSerializer(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Card
        fields = '__all__'

class CardListSerializer(CardSerializer):
    status = serializers.ReadOnlyField()


class CardCreateUserSerializer(CardListSerializer):
    performer = serializers.HiddenField(default=serializers.CurrentUserDefault())


class CardUpdateAdminSerializer(CardSerializer):
    status_list = CardStatus.ADMIN_STATUS_LIST

    def validate_status(self, value):
        if self.instance.performer.id == self.context['request'].user.id:
            self.status_list = CardStatus.STATUS_LIST
        status_list = self.status_list

        if (self.instance.status in status_list and value in status_list):
            status_id = status_list.index(self.instance.status)
            new_status_id = status_list.index(value)
            next_step = (abs(status_id - new_status_id) == 1 or status_id == new_status_id)
            if next_step:
                return value
        elif self.instance.status==value:
            return value
        raise serializers.ValidationError(
            f"You can`t change card status '{self.instance.status}' to status '{value}' ! "
            f"Only 1 step between {status_list}"
        )


class CardUpdateUserSerializer(CardUpdateAdminSerializer):
    performer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status_list = CardStatus.USER_STATUS_LIST


class TaskDashboardUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = TaskDashboardUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = TaskDashboardUser
        fields = ( "id", "username", "password", )