from django.test import TestCase

from mainapp.models import TaskDashboardUser


class TaskDashboardUserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        TaskDashboardUser.objects.create(username = 'Alex', password='123QWEasd@')

    def setUp(self):
        pass

    def test_create_user(self):
        user = TaskDashboardUser.objects.get(id=1)
        field_label =  user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')

    def test_object_name_is_username(self):
        user = TaskDashboardUser.objects.get(id=1)
        expected_obj_name = user.username
        self.assertEquals(expected_obj_name,str(user))



