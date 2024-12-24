from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    #what kind of model we  want to transform and  what fields do we want to transform
    class Meta:
        model = Users
        fields = '__all__'