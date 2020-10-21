class Orc:
    def __init__(self, orc_name, strength, weapon):
        self._name = orc_name
        self._strength = strength
        self._weapon = weapon

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, orc_name):
        if isinstance(orc_name, str):
            self._name = orc_name
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

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, weapon):
        if isinstance(weapon, bool):
            self._weapon = weapon
        else:
            print("type ERROR")

    def fight_with(self, other_orc):
        if self._weapon or other_orc.weapon:
            if self._weapon and not other_orc.weapon:
                self.strength += 1
                print(self)
            elif other_orc.weapon and not self._weapon:
                other_orc.strength += 1
                print(other_orc)
            else:
                self.strength -= 0.5
                other_orc.strength -= 0.5
        else:
            if self > other_orc:
                self.strength += 1
                print(self)
            elif other_orc > self:
                other_orc.strength += 1
                print(other_orc)
            else:
                self.strength -= 0.5
                other_orc.strength -= 0.5

    def __gt__(self, other_orc):
        if self._strength > other_orc.strength:
            return True
        return False

    def __str__(self):
        return "{} {} {}".format(self._name, self._strength, self._weapon)
