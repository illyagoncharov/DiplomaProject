from django.test import TestCase

from cards.models import Card
from mainapp.models import TaskDashboardUser


# Create your tests here.
class CardModelTest(TestCase):

    # @classmethod
    # def setUpTestData(cls):
    #
    #     Card.objects.create(='Alex', password='123QWEasd@')

    def setUp(self):
        test_user = TaskDashboardUser.objects.create(username='Alex', password='123QWEasd@')
        test_user.save()
        test_title = 'title'
        test_task= "some text task"
        test_card = Card.objects.create(user=test_user, title=test_title ,task=test_task, performer=test_user)

    def test_create_user(self):
        user = TaskDashboardUser.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')

    def test_object_name_is_username(self):
        user = TaskDashboardUser.objects.get(id=1)
        expected_obj_name = user.username
        self.assertEquals(expected_obj_name, str(user))

