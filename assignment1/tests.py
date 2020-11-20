from fox_conor import *

import unittest
import sys
from contextlib import contextmanager
from io import StringIO


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class orcTest(unittest.TestCase):
    def test_constructor(self):
        orc1 = Orc("Ogrorg", 4.3, True)
        assert orc1.strength == 4.3, "should be 4.3"
        assert orc1.weapon is True, "should be True"
        with captured_output() as (out, err):
            Orc(1, 1, False)
        output = out.getvalue().strip()
        assert output == "type ERROR", "should be 'type ERROR'"

    def test_attributes(self):
        orc1 = Orc("Ogrorg", 4.3, True)
        orc1.name = "joe"
        with captured_output() as (out, err):
            orc1.name = 3
        output = out.getvalue().strip()
        assert output == "type ERROR", "should be 'type ERROR'"
        assert orc1.name == "joe", "should be 'joe'"
        orc1.strength = -500
        assert orc1.strength == 0.0, "should be 0.0"
        orc1.strength = 555
        assert orc1.strength == 5.0, "should be 5.0"
        orc1.weapon = False
        with captured_output() as (out, err):
            orc1.weapon = 3
        output = out.getvalue().strip()
        assert output == "type ERROR", "should be 'type ERROR'"
        assert orc1.weapon is False, "should be False"

    def test_string(self):
        orc1 = Orc("Ogrorg", 4.3, True)
        with captured_output() as (out, err):
            print(orc1)
        output = out.getvalue().strip()
        assert output == "Ogrorg 4.3 True", "should be 'Ogrorg 4.3 True'"

    def test_greater_than(self):
        orc1 = Orc("Ogrorg", 4.3, True)
        orc2 = Orc("Borg", 1, False)
        orc3 = Orc("Gorg", 0, True)
        orc4 = Orc("Gorgo", 0, True)
        assert orc3 > orc2
        assert orc1 > orc2
        assert orc1 > orc3
        assert (orc3 > orc4) is False

    def test_fight_orc(self):
        orc1 = Orc("Ogrorg", 4.3, True)
        orc2 = Orc("Borg", 1, False)
        orc3 = Orc("Gorg", 0, True)
        with captured_output() as (out, err):
            orc1.fight(orc2)
        output = out.getvalue().strip()
        assert output == "Ogrorg 5.0 True"
        assert orc2.strength == 1.0, "should be 1.0"
        assert orc1.strength == 5.0, "should be 5.0"
        with captured_output() as (out, err):
            orc3.fight(orc2)
        assert orc3.strength == 1.0, "should be 1.0"
        with captured_output() as (out, err):
            orc3.fight(orc2)
            orc3.fight(orc2)
            orc3.fight(orc2)
            orc3.fight(orc2)
        assert orc3.strength == 5.0, "should be 5.0"
        with captured_output() as (out, err):
            orc3.fight(orc1)
        assert orc1.strength == 4.5, "should be 4.5"
        assert orc3.strength == 4.5, "should be 4.5"


class archerTest(unittest.TestCase):
    def test_constructor(self):
        archer = Archer("Legolas", 2.5, "Woodland Kingdom")
        assert archer.strength == 2.5, "should be 2.5"
        assert archer.kingdom == "Woodland Kingdom", "should be 'Woodland Kingdom'"
        with captured_output() as (out, err):
            Archer("Legolas", 2.5, False)
        output = out.getvalue().strip()
        assert output == "type ERROR", "should be 'type ERROR'"

    def test_attributes(self):
        archer = Archer("Legolas", 2.5, "Woodland Kingdom")
        assert archer.strength == 2.5, "should be 2.5"
        archer.strength = 6
        assert archer.strength == 5.0, "should be 5.0"
        assert archer.kingdom == "Woodland Kingdom", "should be 'Woodland Kingdom'"
        with captured_output() as (out, err):
            archer.kingdom = 2
        output = out.getvalue().strip()
        assert output == "type ERROR", "should be 'type ERROR'"

    def test_fight(self):
        a1 = Archer("Legolas", 2.5, "Woodland Kingdom")
        a2 = Archer("Robin Hood", 2, "Sherwood Forest")
        with captured_output() as (out, err):
            a1.fight(a2)
        output = out.getvalue().strip()
        assert output == "fight ERROR", "should be 'fight ERROR'"

    def test_string(self):
        archer = Archer("Legolas", 2.5, "Woodland Kingdom")
        with captured_output() as (out, err):
            print(archer)
        output = out.getvalue().strip()
        assert output == "Legolas 2.5 Woodland Kingdom", "should be 'Legolas 2.5 Woodland Kingdom'"


class knightTest(unittest.TestCase):
    def test_constructor(self):
        knight = Knight("Aragorn", 4.9, "Gondor", [])
        assert knight.strength == 4.9, "should be 4.9"
        assert knight.kingdom == "Gondor", "should be 'Gondor'"
        with captured_output() as (out, err):
            Knight("Aragorn", 2.5, "Gondor", [1, 2, 3])
        output = out.getvalue().strip()
        assert output == "archers list ERROR", "should be 'archers list ERROR'"

    def test_attributes(self):
        a1 = Archer("Legolas", 2.5, "Gondor")
        a2 = Archer("Robin Hood", 2, "Sherwood Forest")
        a3 = Archer("Haldir", 1.9, "Gondor")
        knight = Knight("Aragorn", 4.9, "Gondor", [a1, a2, a3])
        assert knight.archers_list == [a1, a3]
        with captured_output() as (out, err):
            knight.archers_list = [a1, a3, 3]
        output = out.getvalue().strip()
        assert output == "archers list ERROR", "should be 'archers list ERROR'"

    def test_fight(self):
        knight = Knight("Aragorn", 4.9, "Gondor", [])
        knight2 = Knight("Theoden", 2.5, "Rohan", [])
        with captured_output() as (out, err):
            knight.fight(knight2)
        output = out.getvalue().strip()
        assert output == "fight ERROR", "should be 'fight ERROR'"

    def test_string(self):
        a1 = Archer("Legolas", 2.5, "Gondor")
        a2 = Archer("Haldir", 1.9, "Gondor")
        knight = Knight("Aragorn", 4.9, "Gondor", [a1, a2])
        with captured_output() as (out, err):
            print(knight)
        output = out.getvalue().strip()
        assert output == "Aragorn 4.9 Gondor [Legolas 2.5 Gondor, Haldir 1.9 Gondor]"


class characterTest(unittest.TestCase):
    def test_fight_orc_archer(self):
        orc1 = Orc("Ogrorg", 4.3, True)
        orc2 = Orc("Borg", 5.0, False)
        orc3 = Orc("SuperOrc", 5.0, True)
        archer = Archer("Legolas", 2.5, "Woodland Kingdom")
        with captured_output() as (out, err):
            orc2.fight(archer)
        output = out.getvalue().strip()
        assert output == "Legolas 3.5 Woodland Kingdom"
        archer = Archer("Legolas", 2.5, "Woodland Kingdom")
        orc2 = Orc("Borg", 5.0, False)
        with captured_output() as (out, err):
            archer.fight(orc2)
        output = out.getvalue().strip()
        assert output == "Legolas 3.5 Woodland Kingdom"

    def test_fight_orc_knight(self):
        orc1 = Orc("Ogrorg", 4.3, True)
        orc2 = Orc("Borg", 5.0, False)
        orc3 = Orc("SuperOrc", 5.0, True)
        knight = Knight("Aragorn", 4.9, "Gondor", [])
        with captured_output() as (out, err):
            orc1.fight(knight)
        output = out.getvalue().strip()
        assert output == "Aragorn 5.0 Gondor []"
        orc3.fight(knight)
        assert orc3.strength == 4.5, "should be 4.5"
        assert knight.strength == 4.5, "should be 4.5"
        knight = Knight("Aragorn", 4.9, "Gondor", [])
        with captured_output() as (out, err):
            orc2.fight(knight)
        output = out.getvalue().strip()
        assert output == "Aragorn 5.0 Gondor []"
        knight = Knight("Aragorn", 4.9, "Gondor", [])
        orc2 = Orc("Borg", 5.0, False)
        with captured_output() as (out, err):
            knight.fight(orc2)
        output = out.getvalue().strip()
        assert output == "Aragorn 5.0 Gondor []"


if __name__ == '__main__':
    unittest.main(verbosity=2)
