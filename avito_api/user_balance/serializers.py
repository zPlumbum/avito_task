from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'user_balance', 'transactions_allowed',)

    def create(self, validated_data):
        user = super().create(validated_data)
        return user
