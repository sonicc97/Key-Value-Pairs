country = {
    'Country': 'Finland',
    'Position': 'Scandinavia',
    'Population': '5.5M',
    'Language': 'English'
}
print(country)

for key, value in country.items():
    print(key,value)

pitaj = input('Which key we want to change the value of')

if pitaj == 'Language':
    country.pop('Language')
else:
    print('Incorrectly entered key!')

dodati = input('Which value you want to add?')

if dodati == 'Language':
    country.update({'Language': 'Finish'})
else:
    print('Incorrectly entered key')
print(country)