import random

player = []
max_player = 2

while len(player) < max_player:
   
   profile = {
      'name': [],
      'desc': '',
      'size': '',
      'inventory':[],
      'muscle': 0
   }
   #imput player characteristics
   name = input("choose a warrior name:\n ")
   desc = input("Describe warrior - (Thick\Thin\Tall): \n")
   size = int(input('Enter your size in interger: \n'))

   #assigning characteristics to player profile and normalising 
   profile['name'] = name.capitalize()
   player.append(name)
   