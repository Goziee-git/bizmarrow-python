class User:
    classAttribute = "class property"
    __private_classAttribute = "__private_classAttribute"
    
    def __init__(self, username, account):
        self.username = username
        self.__account = account #private

    def public_account(self):
        return self.__account

    def get__account(self):
        return self.__account

    def set__account(self, account):
        if account > 0:
            self.__account = account
            print("Account is active")
        else:
            print("Account is inactive")
        

   