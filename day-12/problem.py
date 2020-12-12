with open('input') as f:
    commands = [(line[0], int(line[1:])) for line in f.read().strip().split()]


# Part 1
class ShipV1(object):

    DIRECTIONS = 'NESW'

    def __init__(self, facing='E'):
        super(ShipV1, self).__init__()
        self.facing = facing
        self.d_x = 0
        self.d_y = 0

    def do_L(self, degrees):
        idx = self.DIRECTIONS.find(self.facing)
        self.facing = self.DIRECTIONS[(idx - int(degrees / 90)) % len(self.DIRECTIONS)]

    def do_R(self, degrees):
        idx = self.DIRECTIONS.find(self.facing)
        self.facing = self.DIRECTIONS[(idx + int(degrees / 90)) % len(self.DIRECTIONS)]

    def do_F(self, value):
        getattr(self, f'do_{self.facing}')(value)

    def do_N(self, value):
        self.d_y -= value

    def do_S(self, value):
        self.d_y += value

    def do_E(self, value):
        self.d_x += value

    def do_W(self, value):
        self.d_x -= value


ship = ShipV1()
for cmd, value in commands:
    getattr(ship, f'do_{cmd}')(value)

print(abs(ship.d_x) + abs(ship.d_y))


# Part 2
class Waypoint(object):

    def __init__(self):
        super(Waypoint, self).__init__()
        self.d_x = 10
        self.d_y = -1

    def do_L(self, degrees):
        for _ in range(int(degrees / 90)):
            self.d_x, self.d_y = self.d_y, -self.d_x

    def do_R(self, degrees):
        for _ in range(int(degrees / 90)):
            self.d_x, self.d_y = -self.d_y, self.d_x

    def do_N(self, value):
        self.d_y -= value

    def do_S(self, value):
        self.d_y += value

    def do_E(self, value):
        self.d_x += value

    def do_W(self, value):
        self.d_x -= value


class ShipV2(object):

    def __init__(self, waypoint=Waypoint(), facing='E'):
        super(ShipV2, self).__init__()
        self.waypoint = waypoint
        self.facing = facing
        self.d_x = 0
        self.d_y = 0

    def do_L(self, degrees):
        self.waypoint.do_L(degrees)

    def do_R(self, degrees):
        self.waypoint.do_R(degrees)

    def do_F(self, value):
        self.d_x += self.waypoint.d_x * value
        self.d_y += self.waypoint.d_y * value

    def do_N(self, value):
        self.waypoint.do_N(value)

    def do_S(self, value):
        self.waypoint.do_S(value)

    def do_E(self, value):
        self.waypoint.do_E(value)

    def do_W(self, value):
        self.waypoint.do_W(value)


ship = ShipV2()
for cmd, value in commands:
    getattr(ship, f'do_{cmd}')(value)

print(abs(ship.d_x) + abs(ship.d_y))
