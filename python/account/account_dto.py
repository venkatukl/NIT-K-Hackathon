class AccountDTO:
    """
    A class that initializes with defaults.
    The builder pattern is used here.
    This class is similar to DTO in Java.
    """
    def __init__(self, account_number, name, account_type, email):
        """
        Initialize account DTO object
        with given details 
        """
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.email = email


class AccountDTOBuilder:
    """
    The builder class.
    It's used to set the values of 
    the AccountDTO object step by step.
    
    Using instance variables and return method we are able
    to retrieve the values in which we are interested.
    """
    def __init__(self):
        """
        Initializes the AccoutDTOBuilder object
        with all fields default
        """
        self.account_number = None
        self.name = None
        self.account_type = None
        self.email = None

    def account_number(self, account_number):
        """
        Sets the account number
        :param account_number
        :return self
        """
        self.account_number = account_number
        return self

    def name(self, name):
        """
        Sets the name
        :param name
        :return self
        """
        self.name = name
        return self

    def account_type(self, account_type):
        """
        Sets the account type
        :param account_type
        :return self
        """
        self.account_type = account_type
        return self

    def email(self, email):
        """
        Sets the email
        :param email
        :return self
        """
        self.email = email
        return self

    def create(self):
        """
        Creates a new AccountDTO objec with the fields input in the builder.
        :return AccountDTO obj
        """
        acc = AccountDTO(self.account_number, self.name, self.account_type, self.email)
        return acc
