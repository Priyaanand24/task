"""
    Auth Validators
"""

import re
from .exception import *


def parse_mobile_number(mobile_number: str) -> bool:
    """
        Mobile number validation
    """
    if not mobile_number:
        raise MobileNumberFormatException("Mobile number shouldn't be empty")
    if type(mobile_number) != str:
        mobile_number = str(mobile_number)

    if len(mobile_number) > 10:
        slice_country_code = mobile_number[:-10]
        if slice_country_code == "+91":
            mobile_number = mobile_number[3:]
            if len(mobile_number) == 10:
                value = re.search(pattern='^[6-9]\d{9}$', string=mobile_number)
                if not value:
                    raise MobileNumberFormatException("Mobile number isn't in the right format")
            else:
                raise MobileNumberLengthException(f'Invalid mobile number:{mobile_number}')
        elif slice_country_code == '91':
            mobile_number = mobile_number[2:]
            if len(mobile_number) == 10:
                value = re.findall(pattern='^[6-9]\d{9}$', string=mobile_number)
                if not value:
                    raise MobileNumberFormatException("Mobile number isn't in the right format")
            else:
                raise MobileNumberLengthException(f'Invalid mobile number:{mobile_number}')
        elif slice_country_code == '+91-':
            mobile_number = mobile_number[4:]
            if len(mobile_number) == 10:
                value = re.findall(pattern='^[6-9]\d{9}$', string=mobile_number)
                if not value:
                    raise MobileNumberFormatException("Mobile number isn't in the right format")
            else:
                raise MobileNumberLengthException(f'Invalid mobile number:{mobile_number}')
        elif slice_country_code == '+91 ':
            mobile_number = mobile_number[4:]
            if len(mobile_number) == 10:
                value = re.findall(pattern='^[6-9]\d{9}$', string=mobile_number)
                if not value:
                    raise MobileNumberFormatException("Mobile number isn't in the right format")
            else:
                raise MobileNumberLengthException(f'Invalid mobile number:{mobile_number}')
        elif slice_country_code == '91-':
            mobile_number = mobile_number[3:]
            if len(mobile_number) == 10:
                value = re.findall(pattern='^[6-9]\d{9}$', string=mobile_number)
                if not value:
                    raise MobileNumberFormatException("Mobile number isn't in the right format")
            else:
                raise MobileNumberLengthException(f'Invalid mobile number:{mobile_number}')
        elif slice_country_code == '91 ':
            mobile_number = mobile_number[3:]
            if len(mobile_number) == 10:
                value = re.findall(pattern='^[6-9]\d{9}$', string=mobile_number)
                if not value:
                    raise MobileNumberFormatException("Mobile number isn't in the right format")
            else:
                raise MobileNumberLengthException(f'Invalid mobile number:{mobile_number}')
        elif slice_country_code == '0':
            mobile_number = mobile_number[1:]
            if len(mobile_number) == 10:
                value = re.findall(pattern='^[6-9]\d{9}$', string=mobile_number)
                if not value:
                    raise MobileNumberFormatException("Mobile number isn't in the right format")
            else:
                raise MobileNumberLengthException(f'Invalid mobile number:{mobile_number}')
        else:
            if len(mobile_number) == 10:
                value = re.findall(pattern='^[6-9]\d{9}$', string=mobile_number)
                if not value:
                    raise MobileNumberFormatException("Mobile number isn't in the right format")
            else:
                raise MobileNumberLengthException(f'Invalid mobile number:{mobile_number}')
    elif len(mobile_number) == 10:
        value = re.search(pattern='^[6-9]\d{9}$', string=mobile_number)

        if not value:
            raise MobileNumberFormatException("Mobile number isn't in the right format")
    else:
        raise MobileNumberLengthException(f'Invalid mobile number:{mobile_number}')

    return True
