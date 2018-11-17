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
        self._angle = new_angle

    def set_tilt(self, tilt) -> None:
        self._tilt = tilt

    def get_state(self):
        s = {
            'angle' : self.get_angle(),
            'tilt' : self.get_tilt()
        }
        s.update(super().get_state())
        return s
