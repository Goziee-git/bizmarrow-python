fred = 5
pete = 4

global_list = []

def name():
   """function to return the sum of pete and fred"""
   dave = fred + pete
   camil = 30
   papa = 10
   global nancy
   nancy = camil + papa
   print(vars()['dave'])
   #return local name() variables
   return vars()

   
def modify_list(local_list):
   local_list.extend(["goziee", "sultan"])
   

which_list = modify_list(global_list)
print(global_list)