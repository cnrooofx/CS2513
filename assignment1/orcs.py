"""CS2513 Assignment 1 Submission.

Script Name: orcs.py
Author: Conor Fox 119322236
"""


class Orc:
    """Class to make an orc character for a video game.

    Attributes:
        _name: String for the name of the orc.
        _strength: Float between 0.0 and 5.0
        _weapon: Boolean value to represent a weapon.
    """

    def __init__(self, orc_name, strength, weapon):
        """Construct an Orc object.

        Args:
            orc_name (str): The name for the Orc
            strength (float): Value between 0 and 5 for the fighting strength
            weapon (bool): True if the Orc has a weapon, False if not
        """
        if isinstance(orc_name, str):
            self._name = orc_name
        else:
            print("type ERROR")
            self._name = 'Name'

        if isinstance(strength, (float, int)):
            if strength < 0:
                self._strength = 0.0
            elif strength > 5:
                self._strength = 5.0
            else:
                self._strength = float(strength)
        else:
            print("type ERROR")
            self._strength = 0.0

        if isinstance(weapon, bool):
            self._weapon = weapon
        else:
            print("type ERROR")
            self._weapon = False

    @property
    def name(self):
        """Return the name of the orc."""
        return self._name

    @name.setter
    def name(self, orc_name):
        """Change the name of the orc."""
        if isinstance(orc_name, str):
            self._name = orc_name
        else:
            print("type ERROR")

    @property
    def strength(self):
        """Return the strength value of the orc."""
        return self._strength

    @strength.setter
    def strength(self, strength):
        """Change the strength value of the orc.

        Notes:
            If the value is less than 0 or greater than 5 it will be truncated
            to the maximum or minimum value.

        Args:
            strength (float): Value between 0 and 5 for the Orc's strength
        """
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
        """Return whether the orc has a weapon or not."""
        return self._weapon

    @weapon.setter
    def weapon(self, weapon):
        """Change if the orc has a weapon.

        Args:
            weapon (bool): True if the Orc has a weapon, otherwise False
        """
        if isinstance(weapon, bool):
            self._weapon = weapon
        else:
            print("type ERROR")

    def fight_with(self, other_orc):
        """Fight with another orc object.

        Notes:
            If one orc has a weapon and the other does not, the one with the
            weapon wins regardless of strength. If both orcs have weapons or
            neither orc has a weapon, the orc with the highest strength wins.
            If both orcs are equal in weapons and strength, both lose.

        Args:
            other_orc: Another Orc object to fight with.
        """
        if isinstance(other_orc, Orc):
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
        """Return True if Orc is stronger than other_orc, otherwise False."""
        if self._weapon or other_orc.weapon:
            if self._weapon and other_orc.weapon:
                if self._strength > other_orc.strength:
                    return True
            elif self._weapon and not other_orc.weapon:
                return True
        elif self._strength > other_orc.strength:
            return True
        return False

    def __str__(self):
        """Return a string of the orc in the form: "name strength weapon"."""
        return "{} {} {}".format(self._name, self._strength, self._weapon)
