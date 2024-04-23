from django.contrib.auth.forms import UserCreationForm
from mainapp.models import TaskDashboardUser


class RegistrationForm(UserCreationForm):

    class Meta:
        model = TaskDashboardUser
        fields = ['username', 'password1', 'password2']