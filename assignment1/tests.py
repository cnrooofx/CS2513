from fox_conor import *

print("----------------\nObject Creation\n----------------")

my_orc = Orc('Orcy', 5, True)

orc1 = Orc('Conor', 1.0, True)
orc2 = Orc('Liam', 4.6, False)
# orc_error = Orc(3, 80, 'True')

print('My Orc:', my_orc)
print('Orc 1:', orc1)
print('Orc 2:', orc2)
# print('Orc w/ Error:', orc_error)

print("----------------\nAttribute Changing\n----------------")

my_orc.name = 5
my_orc.name = 'Changed'
my_orc.strength = 1
print('My Orc:', my_orc)
my_orc.strength = -0.5
print('My Orc:', my_orc)
my_orc.strength = 100
print('My Orc:', my_orc)

print('My Orc:', my_orc)
print('Orc 1:', orc1)
print('Orc 2:', orc2)

print("----------------\nGreater than\n----------------")

if orc1 > orc2:
    print('Conor is stronger')
else:
    print('Liam is stronger')

print(orc2 > orc1)
print(orc1 > orc2)

print("----------------\nFight With\n----------------")

print('Before fighting', orc1, orc2)

orc1.fight(orc2)
orc2.fight(orc1)

print('After fighting', orc1, orc2)

orc2.weapon = True

orc2.fight(orc1)

print('After fighting with weapons', orc1, orc2)

orc1.strength = 5

orc1.fight(orc2)

print('After fighting equal', orc1, orc2)

print("----------------\nTrying to Break\n----------------")

hello = 'hello'

orc1.fight(hello)

# print(orc2 < hello)

orc3 = Orc('Dylan', 2.6, True)
orc4 = Orc('Conor', 2.5, True)

print(orc3, 'vs', orc4)
print(orc3 > orc4)
