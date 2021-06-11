class MobileNumberFormatException(Exception):
    """
        Mobile Number Exceptions
    """

    def __init__(self, value):
        self.error_message = value

    def __str__(self):
        return self.error_message


class MobileNumberLengthException(Exception):
    """
        Password Exceptions
    """

    def __init__(self, value):
        self.error_message = value

    def __str__(self):
        return self.error_message
