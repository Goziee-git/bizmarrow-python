store = []

#create some excep;tion and handle them
try : {}['foo']
except KeyError as e: store.append(e)
try: 1 / 0
except ZeroDivisionError as e: store.append(e)
try: " ".bar()
except AttributeError as e: store.append(e)
try: " ".join(" ") 
except SyntaxError as e: store.append(e)

#loop over the stored errors and print out the eroors
for exception_object in store:
   ec = exception_object.__class__
   print(ec.__name__)
   indent = " +-"
   while ec.__bases__:
      #assign ec's superclass to itself and increament
      ec = ec.__bases__[0]
      print(indent + ec.__name__)
      indent = " " + indent 