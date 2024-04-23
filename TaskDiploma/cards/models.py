from django.db import models
from mainapp.constants import CardStatus
from mainapp.models import TaskDashboardUser


class Card(models.Model):
    title = models.CharField(max_length=25, blank=True, null=True, verbose_name="Title", default='Task title' )
    user = models.ForeignKey(TaskDashboardUser, on_delete=models.CASCADE, related_name='card',
                             verbose_name="Creator")
    task = models.TextField(null=False, max_length=500, blank=False, verbose_name="Task")
    performer = models.ForeignKey(TaskDashboardUser, on_delete=models.DO_NOTHING,
                                  related_name='cardperformer',
                                  verbose_name="Performer")
    date_create = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=CardStatus.STATUS_CHOICES, default='New')

    objects = models.Manager()

    class Meta:
        ordering = ['date_joined']
        db_table = "card"
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    def __str__(self):
        return (
            f'Creator: {self.user} | '
            f'Task: {self.task} | '
            f'Performer: {self.performer} | '
            f'Status: {self.status}'
        )