class Account:
   def __init__(self, account_name, initial_balance=0):
      self.account_name= account_name
      self.__pin = None #private attribute
      self._balance = initial_balance #protected attribute
      self.__transaction = []

   def __validate_pin(self, pin): #private method
      return self.__pin == pin


   def _log_transaction(self, amount, narration, transaction_type): #protected method
      self.__transaction.append({
         "Amount": amount,
         "transaction_type": transaction_type,
         "narration": narration
      })

   def get_withdrawals():
      return 

   def set_pin(self, new_pin):
      if (len(str(new_pin)) == 4):
         self.__pin = new_pin
         return True
      return False

   #demonstrate how a public method can use a private method internally
   def withdrawals(self, amount, pin):
      if not self.__validate_pin(pin):
         return "Invalid Pin"

      if amount > self._balance:
         return "Insufficient funds"

      self._balance -= amount
      self._log_transaction("Withdrawals", amount)
      return f"Withdrawals, ${amount}"
   
   def deposit(self, amount):
      if self._balance > 0:
         self._balance += amount
         self._log_transaction("Deposit", amount)
         return f"Deposited ${amount}"
      return "Invalid Amount"
         

   def get_balance(self, amount, pin):
      if self.__validate_pin(pin):
         return self._balance
      return f"invalid pin"





