import random


class DirectionRandomGenerator:
    def __init__(self, min_X, max_X, min_Y, max_Y):
        self._min_X = min_X
        self._min_Y = min_Y

        self._max_X = max_X
        self._max_Y = max_Y

    def fetch_direction(self):

        x = random.gauss((self._max_X + self._min_X) / 2.0, ((self._max_X) - (self._min_X)) / 2.0)

        y = random.gauss((self._max_Y + self._min_Y) / 2.0, ((self._max_Y) - (self._min_Y)) / 2.0)

        # edge checks
        if(x < self._min_X):
            x = self._min_X
        elif (x > self._max_X):
            x = self._max_X

        if(y < self._min_Y):
            y = self._min_Y
        elif (y > self._max_Y):
            y = self._max_Y

        return (x, y)
