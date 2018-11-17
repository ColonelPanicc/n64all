from controller import Controller
from input import Input, Analog
from input_types import InputTypes
import unittest


class APITest(unittest.TestCase):
    """
    Testing John's API <3
    """

    def setUp(self):
        self._controller = Controller()
        self._analogs = [InputTypes.LEFT_ANALOG, InputTypes.RIGHT_ANALOG, InputTypes.LEFT_TRIGGER, InputTypes.RIGHT_TRIGGER]
        self._buttons = [inputType for inputType in InputTypes if inputType not in self._analogs]

    """
    CONTROLLER CONCRETE CLASS TESTING 
    """

    def test_controller_valid_buttons(self):
        """
        Testing returns valid Input instances for all given input types
        """
        self.assertTrue(all(map(lambda x:  isinstance(self._controller.get_button(x), Input), InputTypes)))

    def test_controller_valid_analog(self):
        """
        Testing returns Analog instances for Analog input buttons
        """
        self.assertTrue(all(map(lambda x: isinstance(self._controller.get_button(x), Analog), self._analogs)))

    def test_controller_valid_non_analog(self):
        """
        Testing returns non Analog (concrete Input) instances for all given input types
        """
        self.assertTrue(all(map(lambda x: not isinstance(self._controller.get_button(x), Analog), self._buttons)))

    def test_controller_invalid(self):
        """
        Testing that errors are raised when a fake button value is requested
        """
        self.assertRaises(ValueError, self._controller.get_button, "FAKE_BUTTON")


if __name__ == "__main__":
    unittest.main()

