from rest_framework.serializers import ModelSerializer
from restaurant.models import Menu

class MenuItemSerializer(ModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'
