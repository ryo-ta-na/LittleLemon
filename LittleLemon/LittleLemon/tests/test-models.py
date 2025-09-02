from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):

    def test_get_menu(self):
        # item = Menu.objects.create(Title="IceCream", Price=10, Inventory=80)
        item = Menu.objects.get(id=1)
        self.assertEqual(item, "Doughnut : 3.50")
