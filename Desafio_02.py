user1_name = input('Usuario 1, favor escribe tu nombre a continuacion => ')
user1_age = int(input(f'{user1_name}, favor escribe tu edad a continuacion => '))
user2_name = input('Usuario 2, favor escribe tu nombre a continuacion => ')
user2_age = int(input(f'{user2_name}, favor escribe tu edad a continuacion => '))

if user1_age > user2_age:
    print(f'{user1_name} tiene mas edad que {user2_name}')
elif user1_age < user2_age:
    print(f'{user2_name} tiene mas edad que {user1_name}')
else:
    print(f'{user1_name} y {user2_name} tienen la misma edad')