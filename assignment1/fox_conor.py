"""CS2513 Assignment 1 Submission.

Script Name: fox_conor.py
Author: Conor Fox 119322236
"""


class Character:
    """Class to make a Character for a video game."""

    def __init__(self, name, strength):
        """Construct a Character object.

        Args:
            name (str): The name for the Character
            strength (float): Value between 0 and 5 for the fighting strength
        """
        if isinstance(name, str):
            self._name = name
        else:
            print('type ERROR')

        if isinstance(strength, (float, int)):
            if strength < 0:
                self._strength = 0.0  # Make value 0 if input is less than 0
            elif strength > 5:
                self._strength = 5.0  # Make value 5 if input is greater than 5
            else:
                self._strength = float(strength)
        else:
            print('type ERROR')

    def __str__(self):
        """Return a string representation of the Character."""
        return '{} {}'.format(self._name, self._strength)

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
        """Change the name of the Character.

        Args:
            name (str): New name for the Character
        """
        if isinstance(name, str):
            self._name = name
        else:
            print('type ERROR')

    @property
    def strength(self):
        """Return the strength value of the Character."""
        return self._strength

    @strength.setter
    def strength(self, strength):
        """Change the strength value of the Character.

        Args:
            strength (float): Value between 0 and 5 for the Characters strength
        """
        if isinstance(strength, (float, int)):
            if strength < 0:
                self._strength = 0.0
            elif strength > 5:
                self._strength = 5.0
            else:
                self._strength = float(strength)
        else:
            print('type ERROR')

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
    """Class to make an Orc character for a video game."""

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
        return '{} {}'.format(super().__str__(), str(self._weapon))

    def __gt__(self, other):
        """Compare the strength of the characters.

        Args:
            other: Another Character object to compare with

        Returns:
            True if the Characrer is stronger than other, otherwise False.
        """
        if isinstance(other, Orc):
            if self.weapon and other.weapon:
                return super().__gt__(other)
            if self.weapon and not other.weapon:
                return True
        # If the Orc isn't fighting an Orc & doesn't have a weapon it will lose
        elif not self._weapon:
            return False
        return super().__gt__(other)

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
            print('type ERROR')


class Human(Character):
    """Class to make a Human character for a video game."""

    def __init__(self, name, strength, kingdom):
        """Construct a Human object.

        Args:
            name (str): The name for the Human
            strength (float): Value between 0 and 5 for the fighting strength
            kingdom (str): The name of the kingdom that the Human belongs to
        """
        super().__init__(name, strength)
        if isinstance(kingdom, str):
            self._kingdom = kingdom
        else:
            print('type ERROR')

    def __str__(self):
        """Return a string representation of the Human."""
        return '{} {}'.format(super().__str__(), self._kingdom)

    @property
    def kingdom(self):
        """Return the name of the Human's kingdom."""
        return self._kingdom

    @kingdom.setter
    def kingdom(self, kingdom):
        """Change the name of the Human's kingdom.

        Args:
            kingdom (str): New kingdom for the Human
        """
        if isinstance(kingdom, str):
            self._kingdom = kingdom
        else:
            print('type ERROR')

    def fight(self, other):
        """Fight with an Orc object.

        Args:
            other: An Orc object to fight with.
        """
        if isinstance(other, Orc):
            Character.fight(self, other)
        else:
            print('fight Error')


class Knight(Human):
    """Class to make a Knight character for a video game."""

    def __init__(self, name, strength, kingdom, archers_list):
        """Construct a Knight object.

        Args:
            name (str): The name for the Knight
            strength (float): Value between 0 and 5 for the fighting strength
            kingdom (str): The name of the kingdom that the Knight belongs to
            archers_list (list): List of Archers led by the Knight
        """
        super().__init__(name, strength, kingdom)
        if isinstance(archers_list, list):
            self._archers_list = archers_list
        else:
            print('type ERROR')

    def __str__(self):
        """Return a string representation of the Knight."""
        archers_string = []
        for archer in self._archers_list:
            archers_string.append(str(archer))
        return '{} {}'.format(super().__str__(), str(archers_string))

    @property
    def archers_list(self):
        """Return the list of the Archers led by the Knight."""
        return self._archers_list

    @archers_list.setter
    def archers_list(self, archers_list):
        """Change the list of the Archers led by the Knight.

        Args:
            archers_list (list): List of Archers in the same kingdom as Knight
        """
        if isinstance(archers_list, list):
            knights_archers = []  # New list to contain satisfactory archers
            for archer in archers_list:
                if isinstance(archer, Archer):  # archer must be of type Archer
                    if archer.kingdom == self._kingdom:  # If same kingdom
                        knights_archers += archer  # Add the archer to the list
                else:
                    print('archers list ERROR')
            self._archers_list = knights_archers  # Set the knights archer list
        else:
            print('type ERROR')


class Archer(Human):
    """Class to make an Archer character for a video game."""
