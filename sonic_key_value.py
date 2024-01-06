test_points = {'Sonic' : [22,97,32], 'Canada': ['Richmond'], 'Test-Number':[77,872,298], 'British': ['Columbia']}
print(test_points)
test_points['Sonic'] = ['Sega','Sonic-Hedgehog']
print(test_points)
test_points2 = test_points['Sonic']
print(test_points2)
if 'British' in test_points:
    print('British Columbia is located in Canada')
else:
    print('British Columbia is not located in Canada')
for key in test_points:
    print(key)
