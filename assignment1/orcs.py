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
        return

    def __gt__(self, other_orc):
        return

    def __str__(self):
        orc_string = "{}, {}, {}".format(self._name, self._strength, self._weapon)
        return orc_string
