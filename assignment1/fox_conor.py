"""CS2513 Assignment 1 Submission.

Script Name: fox_conor.py
Author: Conor Fox 119322236
"""


class Character:
    def __init__(self, name, strength):
        self._name = name
        self._strength = strength

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
        if issubclass(other, Character):
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
        self._weapon = weapon

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, weapon):
        if isinstance(weapon, bool):
            self._weapon = weapon
        else:
            print("type ERROR")

    def __gt__(self, other):
        # if self._weapon or other_orc.weapon:
        #     if self._weapon and other_orc.weapon and \
        #        self._strength > other_orc.strength:
        #         return True
        #     if self._weapon and not other_orc.weapon:
        #         return True
        # elif self._strength > other_orc.strength:
        #     return True
        # return False
        # if isinstance(other, Orc):
        #     if self.weapon and other.weapon:
        #         return self > other
        #     if self.weapon and not other.weapon:
        #         return True
        # elif not self._weapon:
        #
        # return Character.__gt__(self, other)
        pass


class Human(Character):
    def __init__(self, name, strength, kingdom):
        Character.__init__(self, name, strength)
        self._kingdom = kingdom

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


class Archer(Human):
    pass


class Knight(Human):
    def __init__(self, name, strength, kingdom):
        Human.__init__(self, name, strength, kingdom)
        self._archers_list = []

    def __str__(self):
        return Human.__str__(self) + ' ' + str(self._archers_list)


def main():
    # a1 = Archer('Conor', 1.0, 'Gondor')
    # print(a1.name)
    k1 = Knight('Bob', 4.5, 'Gondor')
    print(k1)
    o1 = Orc('Ogrorg', 5.0, False)
    print(o1 > k1)


if __name__ == '__main__':
    main()
