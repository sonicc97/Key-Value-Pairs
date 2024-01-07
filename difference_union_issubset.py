#ISSUBSET - Check whether a set like 'chat' is a subset of another.
friends = {"Emma", "Jen", "Rob", "Ed"}
chat = {"Jen", "Ed"}
check = chat.issubset(friends)
print(check)

#UNION - We get one element from each variable
classmates = {"Sue", "Paul", "John", "David", "De Gea"}
friends = {"Sonic", "Paul", "David"}
check = classmates.union(friends)
print(check)

#INTERSECTION - Element found in both sets like 'Paul' and 'David'
classmates = {"Sue", "Paul", "John", "David", "De Gea"}
friends = {"Sonic", "Paul", "David"}
check = classmates.intersection(friends)
print(check)

#DIFFERENCE - Between 'classmates' and 'friends'
classmates = {"Sue", "Paul", "John", "David", "De Gea"}
friends = {"Sonic", "Paul", "David"}
check = classmates.difference(friends)
print(check)