class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name

    def __str__(self):
        return self.method_name


class MealyMachine:
    def __init__(self):
        self.state = 'A'

    def put(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            return 2
        elif self.state == 'C':
            self.state = 'F'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            self.state = 'D'
            return 9

    def spawn(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'E':
            self.state = 'B'
            return 7
        else:
            raise MealyError("spawn")


def test():
    machine = main()
    assert machine.put() == 0
    assert machine.put() == 2
    assert machine.spawn() == 1
    assert machine.spawn() == 3
    try:
        machine.spawn()
    except MealyError as e:
        assert str(e) == "spawn"
        assert e.method_name == "spawn"
    assert machine.put() == 5
    assert machine.put() == 6
    assert machine.put() == 8
    try:
        machine.spawn()
    except MealyError as e:
        assert str(e) == "spawn"
        assert e.method_name == "spawn"
    assert machine.put() == 9
    assert machine.put() == 5
    assert machine.spawn() == 7
    assert machine.spawn() == 1
    assert machine.put() == 4


def main():
    return MealyMachine()
