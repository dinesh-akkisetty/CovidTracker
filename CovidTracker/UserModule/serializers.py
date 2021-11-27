from rest_framework import serializers
from .models import User, SelfAssessment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'phoneNumber', 'zipcode']

    # def create(self, validated_data):
    #     user =