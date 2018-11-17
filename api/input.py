class Input:

    def __init__(self):
        self._hold_time = 0
        self._active = False

    def get_active(self) -> bool:
        return self._active

    def get_held_time(self) -> int:
        return self._hold_time

    def toggle(self) -> None:
        self._active = not self._active

    def set_active(self, new_active) -> None:
        self._active = new_active

    def set_hold_time(self, new_hold_time) -> None:
        if not isinstance(new_hold_time, int):
            raise TypeError("New hold time needs to be an int dude")
        elif new_hold_time is None:
            raise ValueError("New hold time can't be None you dingus")
        self._hold_time = new_hold_time

    def get_state(self):
        return {'active' : self.get_active()}


class Analog(Input):

    def __init__(self):
        super().__init__()
        self._angle, self._tilt = 0, 0

    def get_angle(self) -> int:
        return self._angle

    def get_tilt(self) -> int:
        return self._tilt

    def set_angle(self, new_angle) -> None:
        if not isinstance(new_angle, float):
            raise TypeError("New angle needs to be a float dude")
        elif new_angle is None:
            raise ValueError("New angle can't be None you dingus")
        elif new_angle < 0:
            raise ValueError("New angle is a little boi")
        elif new_angle > 360:
            raise ValueError("New angle is a big boi")
        self._angle = new_angle

    def set_tilt(self, tilt) -> None:
        if not isinstance(tilt, float):
            raise TypeError("Tilt needs to be a float dude")
        elif tilt is None:
            raise ValueError("Tilt can't be None you dingus")
        elif tilt < 0:
            raise ValueError("Tilt is a little boi")
        elif tilt > 1:
            raise ValueError("Tilt is a big boi")
        self._tilt = tilt

    def get_state(self):
        s = {
            'angle': self.get_angle(),
            'tilt': self.get_tilt()
        }
        s.update(super().get_state())
        return s
