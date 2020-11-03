"""CS2513 Assignment 1 Submission.

Script Name: fox_conor.py
Author: Conor Fox 119322236
"""


class Character:
    """Class to make a Character for a video game.

    Attributes:
        _name (str): Name of the character (Protected)
        _strength (float): Strength value between 0.0 and 5.0 (Protected)
    """

    def __init__(self, name, strength):
        """Construct a Character object.

        Args:
            name (str): The name for the Character
            strength (float): Value between 0 and 5 for the fighting strength
        """
        if isinstance(name, str):
            self._name = name
        else:
            print("type ERROR")

        if isinstance(strength, (float, int)):
            if strength < 0:
                self._strength = 0.0  # Make value 0 if input is less than 0
            elif strength > 5:
                self._strength = 5.0  # Make value 5 if input is greater than 5
            else:
                self._strength = float(strength)
        else:
            print("type ERROR")

    def __str__(self):
        """Return a string representation of the Character."""
        return "{} {}".format(self._name, self._strength)

    def __gt__(self, other):
        """Compare the strength of the characters.

        Args:
            other: Another Character object to compare with

        Returns:
            True if the Characrer is stronger than other, otherwise False.
        """
        if self._strength > other.strength:
            return True
        return False

    @property
    def name(self):
        """Return the name of the Character."""
        return self._name

    @name.setter
    def name(self, name):
        """Change the name of the Character."""
        if isinstance(name, str):
            self._name = name
        else:
            print("type ERROR")

    @property
    def strength(self):
        """Return the strength value of the Character."""
        return self._strength

    @strength.setter
    def strength(self, strength):
        """Change the strength value of the Character.

        Notes:
            If the value is less than 0 or greater than 5 it will be truncated
            to the maximum or minimum value.

        Args:
            strength (float): Value between 0 and 5 for the characters strength
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

    def fight(self, other):
        """Fight with another Character object.

        Notes:
            If one Character is stronger than the other, then the stronger
            Character wins and it's strength is increased by 1.
            If neither Character is stronger, both lose and both strengths are
            decreased by 0.5.

        Args:
            other: Another Character object to fight with.
        """
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


class Orc(Character):
    """Class to make an Orc character for a video game.

    Attributes:
        _name (str): Name of the orc (Protected)
        _strength (float): Orc strength value between 0.0 and 5.0 (Protected)
        _weapon (bool): Boolean value to represent a weapon (Protected)
    """

    def __init__(self, name, strength, weapon):
        """Construct an Orc object.

        Args:
            name (str): The name for the Orc
            strength (float): Value between 0 and 5 for the fighting strength
            weapon (bool): True if the Orc has a weapon, False if not
        """
        Character.__init__(self, name, strength)
        if isinstance(weapon, bool):
            self._weapon = weapon
        else:
            print('type ERROR')

    def __str__(self):
        """Return a string representation of the Orc."""
        return Character.__str__(self) + ' ' + str(self._weapon)

    def __gt__(self, other):
        """Compare the strength of the characters.

        Args:
            other: Another Character object to compare with

        Returns:
            True if the Characrer is stronger than other, otherwise False.
        """
        if isinstance(other, Orc):
            if self.weapon and other.weapon:
                return Character.__gt__(self, other)
            if self.weapon and not other.weapon:
                return True
        # If the Orc isn't fighting an Orc doesn't have a weapon it will lose
        elif not self._weapon:
            return False
        return Character.__gt__(self, other)

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


class Human(Character):
    """Class to make a Human character for a video game.

    Attributes:
        _name (str): Name of the Human (Protected)
        _strength (float): Strength value between 0.0 and 5.0 (Protected)
        _kingdom (str): The name of the character's kingdom (Protected)
    """

    def __init__(self, name, strength, kingdom):
        """Construct a Human object.

        Args:
            name (str): The name for the Human
            strength (float): Value between 0 and 5 for the fighting strength
            kingdom (str): The name of the kingdom that the Human belongs to
        """
        Character.__init__(self, name, strength)
        if isinstance(kingdom, str):
            self._kingdom = kingdom
        else:
            print('type ERROR')

    def __str__(self):
        """Return a string representation of the Human."""
        return Character.__str__(self) + ' ' + self._kingdom

    @property
    def kingdom(self):
        """Return the name of the Character's kingdom."""
        return self._kingdom

    @kingdom.setter
    def kingdom(self, kingdom):
        """Change the name of the Character's kingdom."""
        if isinstance(kingdom, str):
            self._kingdom = kingdom
        else:
            print('type ERROR')

    def fight(self, other):
        """Fight with an Orc object.

        Notes:
            Humans can only fight with Orcs, not other Humans

        Args:
            other: An Orc object to fight with.
        """
        if isinstance(other, Orc):
            Character.fight(self, other)
        else:
            print('fight Error')


class Knight(Human):
    """Class to make a Knight character for a video game.

    Attributes:
        _name (str): Name of the Knight (Protected)
        _strength (float): Strength value between 0.0 and 5.0 (Protected)
        _kingdom (str): The name of the Knight's kingdom (Protected)
        _archers_list (list): Archers led by the Knight (Protected)
    """

    def __init__(self, name, strength, kingdom, archers_list):
        """Construct a Knight object.

        Args:
            name (str): The name for the Human
            strength (float): Value between 0 and 5 for the fighting strength
            kingdom (str): The name of the kingdom that the Human belongs to
            archers_list (list): List of Archers led by the Knight
        """
        Human.__init__(self, name, strength, kingdom)
        if isinstance(archers_list, list):
            self._archers_list = archers_list
        else:
            print('type ERROR')

    def __str__(self):
        """Return a string representation of the Knihgt."""
        return Human.__str__(self) + ' ' + str(self._archers_list)

    @property
    def archers_list(self):
        """Return the list of the Archers led by the Knight."""
        return self._archers_list

    @archers_list.setter
    def archers_list(self, archers_list):
        """Change the list of the Archers led by the Knight."""
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
    """Class to make a Archer character for a video game.

    Attributes:
        _name (str): Name of the Archer (Protected)
        _strength (float): Strength value between 0.0 and 5.0 (Protected)
        _kingdom (str): The name of the Archer's kingdom (Protected)
    """


def main():
    """Test methods for the classes."""
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
