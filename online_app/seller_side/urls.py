from django.urls import path
from .views import *
from rest_framework import routers

from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from .Rest_api.user_accounts import *
from django.urls import path

router = DefaultRouter()
router.register('account', AccountViewSet)
router.register('store', StoreViewSet)
router.register('product', ProductViewSet)
router.register('customers', CustomersViewSet)
router.register('store', StoreViewSet)


# router.register('login', LoginViewset)


urlpatterns = [
    path('seller_side/', include(router.urls)),
    path('hello/', HelloView.as_view(), name='hello'),

]
