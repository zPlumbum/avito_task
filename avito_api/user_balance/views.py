from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import F
from rest_framework.views import APIView
from rest_framework.serializers import ValidationError

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserBalanceView(APIView):

    def post(self, request):
        user_id = request.data['user_id']
        value = request.data['value']
        user = User.objects.filter(id=user_id).first()

        if user.user_balance + value < 0:
            raise ValidationError("User's balance can't be less than 0")
        else:
            User.objects.filter(id=user_id).update(user_balance=F('user_balance') + value)

        return Response('Transaction complete!')


class UserToUserTransactionView(APIView):

    def post(self, request):
        from_user_id = request.data['from_user_id']
        to_user_id = request.data['to_user_id']
        value = request.data['value']
        from_user = User.objects.filter(id=from_user_id).first()

        if value < 0:
            raise ValidationError("Value can't be less than 0")
        elif (from_user.user_balance < value) or not from_user.transactions_allowed:
            raise ValidationError("User does not have enough money in the account or has no permission for transaction")
        else:
            User.objects.filter(id=from_user_id).update(user_balance=F('user_balance') - value)
            User.objects.filter(id=to_user_id).update(user_balance=F('user_balance') + value)

        return Response('Transaction completed!')
