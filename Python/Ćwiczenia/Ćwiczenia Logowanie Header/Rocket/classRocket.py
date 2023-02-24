import random
from math import sqrt


class Rocket:
    nextId = 1

    def __init__(self, speed=1, altitude=0, x=0):
        self.altitude = altitude
        self.speed = speed
        self.x = x
        self.Id = Rocket.nextId
        Rocket.nextId += 1

    def moveUp(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rocket is actually at altitude: " + str(self.altitude)


class RocketBoard:
    def __init__(self, amountOfRockets=5):
        self.rockets = [Rocket(random.randint(1, 6,), x=random.randint(1, 4,))
                        for _ in range(amountOfRockets)]

        for _ in range(10):
            rocketIndexToMove = random.randint(0, len(self.rockets) - 1)
            self.rockets[rocketIndexToMove].moveUp()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].altitude = value
        return "tralala"

    @staticmethod
    def measure_distance(rocket1, rocket2):
        ab = (rocket1.altitude - rocket2.altitude) ** 2
        bc = (rocket1.x - rocket2.x) ** 2
        return sqrt(ab + bc)

    def __len__(self):
        return len(self.rockets)
