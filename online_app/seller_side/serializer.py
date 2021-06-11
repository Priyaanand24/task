from rest_framework import serializers
from .models import *
from .validator import *

import logging

logger = logging.getLogger(__name__)


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = "__all__"

    def validate(self, attrs):
        mobile_number = attrs.get('mobile_number', None)

        if mobile_number is not None:
            try:
                parse_mobile_number(mobile_number=mobile_number)
            except MobileNumberLengthException as e:
                logger.error(f'Invalid Mobile number length {e}')
                raise serializers.ValidationError(f'Invalid Owner Mobile number')
            except MobileNumberFormatException as e:
                logger.error(f'Invalid  Mobile Number Format: {e}')
                raise serializers.ValidationError(f'Please Give valid format mobile '
                                                  f'number format for Owner Mobile')
        return attrs


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"

# class LoginSerializer(serializers.ModelSerializer):
#     mobile_number = serializers.CharField(required=True, allow_null=False)
#     otp = serializers.IntegerField(required=True, allow_null=False)
#
#     def validate(self, attrs):
#         """
#             Login serializer validation
#         """
#         mobile_number = attrs.get('mobile_number', None)
#         otp = attrs.get('otp', None)
#
#         if mobile_number is None:
#             raise serializers.ValidationError(f'mobile_number should not be empty')
#
#         if otp is None:
#             raise serializers.ValidationError(f'otp should not be empty')
#
#         return attrs

