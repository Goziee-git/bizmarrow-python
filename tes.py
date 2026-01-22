from pathlib import Path


#CONSTANTS
file_path = Path("/mnt/c/Users/USER-PC/py-basics/learning-python/tes.txt")
new_team  = []
team = {
   'name': [],
   'location': 'abuja'
}

player_name = []
max_player = 2

#loop through the dictonary key "name"
while  player_name != max_player:
   player_name = input('enter name here: \n')
   team['name'].append(player_name)
   for names in team['name']:
      new_team.append(names)
   print(new_team)
   
with file_path.open('a') as f:
   f.write(f"a new list of names in a new file: {new_team}")
