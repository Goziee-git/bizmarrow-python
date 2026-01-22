#Role playing combat game
#import modules
import random

#set up constant data

stock = {'shield': (50,20,50),
         'sword': (60,60,20),
         'dagger': (40,90,30),
         'halberd': (80,70,40),
         'club': (50,20,30),
         'flail': (30,30,50),
         'hammer': (101,100,0),
         'armour': (10,5,50),
         'pole': (10,5,70),
         'rope': (30,20,10)
         }

armour_types = ('sheild', 'dagger', 'armour')
hits = ('hits', 'bashes', 'smites', 'whacks', 'shreds', 'mutilates', 'lacerates', 'annihilates')
misses = ('misses', 'nearly hits', 'fail to connect', 'swipes widly at', 'fails ineffectively at', 'get nowhere near', 'hits self in the foot')
damage_report = ('small insult', 'flesh wound', 'deep slash', 'ragged gash', 'savage laceration', 'fractured rib-cage')
life_changing = ('a scar', 'bruising', 'serious blood-loss', 'total debilitation', 'chronic concussion', 'multiple fractures')


# preferences
#set to TRUE to trace varaibles
trace = False
max_players = 2
#this is a global varaible
players = []
#generate characters
while len(players) < max_players:
   print()
   print("New Character")
   print()
   #Create empty profile dictionary
   profile = {
      'Name': "",
      'Desc': "",
      'Gender': "",
      'Race': "",
      'Muscle': 0,
      'Brainz': 0,
      'Speed': 0,
      'Charm': 0,
      'Life': 0,
      'Magic': 0,
      'prot': 0,
      'gold': 0,
      'inventory': []
      }

      #Prompt user for user-defined information(Name, Desc, Gender, Race)
   name = input('what is your name?\n ')
   desc = input('Describe yourself:\n ')
   gender = input('Gender? (male/female/unsure):\n')
   race = input('What Race are you? - (Pixie/vulcan/Gelfing/Troll):\n ')

      #Validate user input
   profile['Name'] = name.capitalize()
   profile['Desc'] = desc.capitalize()
   gender = gender.lower()
   if gender.startswith('f'):
      profile['Gender'] = 'female'
   elif gender.startswith('m'):
      profile['Gender'] = 'male'
   else:
      profile['Gender'] = 'neutral'

   race = race.capitalize()
   if race.startswith('P'):
      profile['Race'] = 'Pixie'
   elif race.startswith('V'):
      profile['Race'] = 'Vulcan'
   elif race.startswith('T'):
      profile['Race'] = 'Troll'
   elif race.startswith('G'):
      profile['Race'] = 'Gelfing'
   else:
      profile['Race'] = 'Goblin'

   #generate stats ('Muscle, Brains, Speed, charm)
   profile['Muscle'] = random.randint(3,33) + random.randint(3,33) + random.randint(3,33)
   profile['Brainz'] = random.randint(3,33) + random.randint(3,33) + random.randint(3,33)
   profile['Speed'] = random.randint(3,33) + random.randint(3,33) + random.randint(3,33)
   profile['charm'] = random.randint(3,33) + random.randint(3,33) + random.randint(3,33)
       
    # Work out combat stats (life, magic, prot, gold)
   life = (profile['Muscle'] + (profile['Speed']/2) + random.randint(9,49))/2
   magic = (profile['Brainz'] + (profile['Charm']/2) + random.randint(9,49))/2
   prot = (profile['Speed'] + (profile['Brainz']/2) + random.randint(9,49))/2
   gold = random.randint(9,49) + random.randint(9,49) + random.randint(9,49)

   #validate stats
   if life > 0 and life < 100:
      profile['life'] = life
   else:
      life = random.randint(9,99)
   if magic > 0 and magic < 100:
      profile['magic'] = magic
   else:
      magic = random.randint(9,99)
   if prot > 0 and prot < 100:
      profile['prot'] = prot
   else:
      prot = random.randint(9,99)
   if gold > 0:
      profile['gold'] = gold
   else:
      gold = random.randint(9,99)

   #output character sert
   fancy_line = "<~~==|#|==~~++**\@/**++~~==|#|==~~>"
   print()
   print(fancy_line)
   print("\t", profile['Name'])
   print("\t", profile['Race'], profile['Gender'])
   print("\t", profile['Desc'])
   print(fancy_line)
   print()
   print("\tMuscle: ", profile['Muscle'], "\tlife: ", profile['life'])
   print("\tBrainz: ", profile['Brainz'], "\tmagic: ", profile['magic'])
   print("\tSpeed: ", profile['Speed'], "\tprotection: ", profile['prot'])
   print("\tCharm: ", profile['Charm'], "\tgold: ", profile['gold'])
   print()

   #prompt user to buy some equipment
   purchase = input('Would you like to buy some equipment? ')
   while purchase != 'done':
      #display shop stock list with prices
      print()
      print("<==|#|==\SHOP/==|#|==>")
      for item in stock:
         print("\t", item, stock[item][0])
         print("<==|#|==\@@@@/==|#|==>")
         print()
         print('You have', profile['gold'], 'gold.')
         #prompt user to make a purchase
         purchase = input('Please choose an item or type "done" to quit. ')
         #if the item is in stock and the player has enough gold to buy
         if purchase in stock:
            if stock[purchase][0] <= profile['gold']:
               print("You buy a ", purchase, "for", stock[purchase][0], \
                  "gold pieces. ")
               profile['gold'] -= stock[purchase][0]
               profile['inventory'].append(purchase)
               print('You have a'," ".join(profile['inventory']),\
                  "in yout bag.")
               print("you have", profile['gold'], "left.")
            elif purchase == 'done':
               break
            else:
               print("you dont have enough gold to buy that.")
         else:
            print("We dont have", purchase, "in stock.")
      print("you own a", " ".join(profile['inventory']))

      #prompt user to enter into combat and choose a weapon
      print(profile['Name'], "Are you ready for mortal combat?")
      weapon = input('Then chooose your weapon: ')
      #The weapin must be in the player inventory
      #Default to first if weapon is available.
      weapon = weapon.lower()
      if weapon in profile['inventory']:
         profile['weapon'] = stock[weapon]
      else:
         profile['weapon'] = (0,20,50)
      #see if player has any armour
      profile['armour'] = (0,0,50)
      for armour_type in armour_types:
         if armour_type in profile['inventory']:
            profile['armour'] = armour_types
      print(profile['Name'], "is now ready for battle.")
      #Add new player to the list
      players.append(profile)

#combat
print()
print("Then let the combat begin!")
print()
vel_max = 23
vel_min = 1
dam_max = 23
# Loop while a player is still alive
while players[0]['life'] > 0 and players[1]['life'] > 0:
   for attacker, player in enumerate(players):
      target = int(not bool(attacker))
      life_left = players[target]['life']
      # Calculate velocity of blow
      attack_speed = players[attacker]['Speed']
      weapon_speed = players[attacker]['weapon'][2]
      attack_chance = random.randint(1,players[attacker]['Brainz'])
      attack_velocity = attack_speed + weapon_speed + attack_chance
      target_prot = players[target]['prot']
      armour_speed = players[target]['armour'][2]
      target_velocity = target_prot + armour_speed
      velocity = (attack_velocity - target_velocity) / 2
      if trace:
         print("\t", velocity)
      if velocity > 0:
         if velocity > vel_max
            vel_max = velocity
         hit_type = int(7 * velocity / vel_max)
         if hit_type > 7:
            hit_type = 7
         if trace:
            print("\t\tHit#", hit_type)
         print(players[attacker]['Name'], hits[hit_type], \
         players[target]['Name']),
         continue
      # Calculate damage inflicted by blow
      attack_strength = players[attacker]['Muscle']
      weapon_damage = players[attacker]['weapon'][1]
      attack_damage = attack_strength + weapon_damage + velocity
      target_strength = players[target]['Muscle']
      armour_strength = players[target]['armour'][1]
      target_chance = random.randint(9,players[target]['Brainz'])
      target_defence = target_strength + armour_strength + target_chance
      potential_damage = (attack_damage - target_defence)
      if potential_damage < 1:
         potential_damage = 2
      damage = float(random.randint(1,potential_damage))
      if trace:
         print()
      print("\t\tDamage:", damage)
      if damage > dam_max:
         dam_max = damage
      # Print damage report
      damage_type = int(7 * damage/dam_max)
      if damage_type > 7:
         damage_type = 7
      if trace:
         print("\t\t\tDamage#", damage_type)
      change_type = int(5 * damage/life_left)
      if change_type > 7:
         change_type = 7
      if trace:
         print("\t\t\t\tChange#", change_type)
      print("inflicting a", damage_report[damage_type], \
            "and", life_changing[change_type])
      # Inflict damage on target.
      players[target]['life'] -= damage
      # Check whether target is still alive or not.
      if players[target]['life'] <= 0:
         # Print winner
         print()
         print(players[target]['Name'], "collapses in a pool of blood")
         print(players[attacker]['Name'], "wins the fight.")
         print()
         break
if trace:
   print()
   print("\t\tmax", dam_max, vel_max, ":: min", vel_min)
   print()








