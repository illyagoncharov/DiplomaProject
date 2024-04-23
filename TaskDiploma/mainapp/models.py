from django.contrib.auth.models import AbstractUser


class TaskDashboardUser(AbstractUser):

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username


