"""CS2513 Assignment 1 Submission.

Script Name: fox_conor.py
Author: Conor Fox 119322236
"""


class Character:
    def __init__(self, name, strength):
        if isinstance(name, str):
            self._name = name
        else:
            print("type ERROR")

        if isinstance(strength, (float, int)):
            if strength < 0:
                self._strength = 0.0
            elif strength > 5:
                self._strength = 5.0
            else:
                self._strength = float(strength)
        else:
            print("type ERROR")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print("type ERROR")

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):
        if isinstance(strength, (float, int)):
            if strength < 0:
                self._strength = 0.0
            elif strength > 5:
                self._strength = 5.0
            else:
                self._strength = float(strength)
        else:
            print("type ERROR")

    def fight(self, other):
        if isinstance(other, Character):
            if self > other:
                self.strength += 1
                print(self)
            elif other > self:
                other.strength += 1
                print(other)
            else:
                self.strength -= 0.5
                other.strength -= 0.5

    def __str__(self):
        return "{} {}".format(self._name, self._strength)

    def __gt__(self, other):
        if self._strength > other.strength:
            return True
        return False


class Orc(Character):
    def __init__(self, name, strength, weapon):
        Character.__init__(self, name, strength)
        if isinstance(weapon, bool):
            self._weapon = weapon
        else:
            print('type ERROR')

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, weapon):
        if isinstance(weapon, bool):
            self._weapon = weapon
        else:
            print("type ERROR")

    def __str__(self):
        return Character.__str__(self) + ' ' + str(self._weapon)

    def __gt__(self, other):
        if isinstance(other, Orc):
            if self.weapon and other.weapon:
                return Character.__gt__(self, other)
            if self.weapon and not other.weapon:
                return True
        elif not self._weapon:
            return False
        return Character.__gt__(self, other)


class Human(Character):
    def __init__(self, name, strength, kingdom):
        Character.__init__(self, name, strength)
        if isinstance(kingdom, str):
            self._kingdom = kingdom
        else:
            print('type ERROR')

    def __str__(self):
        return Character.__str__(self) + ' ' + self._kingdom

    @property
    def kingdom(self):
        return self._kingdom

    @kingdom.setter
    def kingdom(self, kingdom):
        if isinstance(kingdom, str):
            self._kingdom = kingdom
        else:
            print('type ERROR')

    def fight(self, other):
        if isinstance(other, Orc):
            Character.fight(self, other)
        else:
            print('fight Error')


class Knight(Human):
    def __init__(self, name, strength, kingdom, archers_list=[]):
        Human.__init__(self, name, strength, kingdom)
        if isinstance(archers_list, list):
            self._archers_list = archers_list
        else:
            print('type ERROR')

    def __str__(self):
        return Human.__str__(self) + ' ' + str(self._archers_list)

    @property
    def archers_list(self):
        return self._archers_list

    @archers_list.setter
    def archers_list(self, archers_list):
        if isinstance(archers_list, list):
            knights_archers = []  # New list to contain satisfactory archers
            for item in archers_list:
                if isinstance(item, Archer):  # The item must be an Archer
                    if item.kingdom == self._kingdom:  # If same kingdom
                        knights_archers += item  # Add the archer to the list
                else:
                    print('archers list ERROR')
            self._archers_list = knights_archers  # Set the knights archer list
        else:
            print('type ERROR')


class Archer(Human):
    pass


def main():
    a1 = Archer('Conor', 1.0, 'Gondor')
    print(a1.name)
    k1 = Knight('Bob', 4.5, 'Gondor')
    print(k1)
    o1 = Orc('Ogrorg', 3.6, True)
    o2 = Orc('Borg', 0, True)
    print(o2 > k1)
    # k1.fight(o1)
    print(a1)
    print(k1)
    print(o1)


if __name__ == '__main__':
    main()
