from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user_balance.views import UserViewSet, UserBalanceView, UserToUserTransactionView


router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_balance/', UserBalanceView.as_view(), name='user_balance'),
    path('transaction/', UserToUserTransactionView.as_view(), name='transaction'),
    path('api/', include(router.urls)),
]
