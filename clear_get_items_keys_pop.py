#CLEAR - Fuction
team1 = {'Gandalf': '+1 43-4324', 'Aragorn': '+1 443-777', 'Frodo': '+1 837-544'}
print(team1)
clear = team1.clear()
print(clear)

#GET - Find the input
team2 = {'Gandalf': '+1 43-4324', 'Aragorn': '+1 443-777', 'Frodo': '+1 837-544'}
find = team2.get('Gandalf', 'Input was found')
print(find)
find2 = team2.get('Legolas', 'Input was not found')
print(find2)

#ITEMS - Returns all dictionary keys
#FOR - loop displays the  dictionary
#KEYS - Returns only dictionary keys
team3 = {'Gandalf': '+1 43-4324', 'Aragorn': '+1 443-777', 'Frodo': '+1 837-544'}
check_items = team3.items()
print(check_items)
for key, value in team3.items():
    print(key, value)
team3.keys()
print(team3)
for key in team3.keys():
    print(key)

#POP - Returns a value to a specified key and removes that key
lotr_4 = {'Gandalf': '+1 43-4324', 'Aragorn': '+1 443-777', 'Frodo': '+1 837-544'}
check_lotr = lotr_4.pop('Frodo', 'Frodo is found')
print(check_lotr)
print(lotr_4)
check_lotr = lotr_4.pop('Samwise', 'Samwise is not found')
print(check_lotr)
print(lotr_4)

#POPITEM - Displays the last value and deletes it
lotr_5 = {'Gandalf': '+1 43-4324', 'Aragorn': '+1 443-777', 'Frodo': '+1 837-544'}
print(lotr_5)
key, value = lotr_5.popitem()
print(key, value)
print(lotr_5)

#VALUES - Returns all dictionary values without their keys
lotr_6 = {'Gandalf': '+1 43-4324', 'Aragorn': '+1 443-777', 'Frodo': '+1 837-544'}
print(lotr_6)
lotr_6.values()
for key in lotr_6.values():
    print(key)