from controller import Controller
from input import Input, Analog
from input_types import InputTypes
from random import random, randint
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

    """
    INPUT CONCRETE CLASS TESTING 
    """

    def test_input_constructor_inactive(self):
        """
        Tests that all the buttons in the controller default as inactive
        """
        self.assertTrue(all(map(lambda x: not self._controller.get_button(x).get_active(), InputTypes)))

    def test_input_constructor_hold_time(self):
        """
        Tests that all the buttons in the controller default as hold time
        """
        self.assertTrue(all(map(lambda x: 0 == self._controller.get_button(x).get_held_time(), InputTypes)))

    def test_input_set_hold_time(self):
        """
        Tests that the hold time for a button can be updated
        """

        # generate a list of random times to hold the buttons for
        new_hold_times = [randint() for _ in range(len(InputTypes))]

        # call set_active on these flips
        for i, input_type in enumerate(InputTypes):
            self._controller.get_button(input_type).set_active(new_hold_times[i])

        # check that the ones with set_active called have been flipped by comparing to flips
        self.assertEqual([self._controller.get_button(input_type).get_active() for input_type in InputTypes],
                         new_hold_times)

    def test_input_set_active(self):
        """
        Randomly select input types to flip, then check that their active state is flipped
        """

        # random flips
        flips = [random() < 0.5 for _ in range(len(InputTypes))]

        # call set_active on these flips
        for i, input_type in enumerate(InputTypes):
            self._controller.get_button(input_type).set_active(flips[i])

        # check that the ones with set_active called have been flipped by comparing to flips
        self.assertEqual([self._controller.get_button(input_type).get_active() for input_type in InputTypes],
                         flips)

    def test_input_set_held_time_invalid_negative(self):
        """
        Checking that negative values aren't allowed for new held-times for buttons
        """
        self.assertRaises(ValueError, self._controller.get_button(InputTypes.LEFT_ANALOG).set_hold_time(-1))

    def test_input_set_held_time_invalid_type(self):
        """
        Checking that non-int and non-float values aren't allowed for new held-times for buttons
        """
        self.assertRaises(ValueError, self._controller.get_button(InputTypes.LEFT_ANALOG).set_hold_time("LONG TIME"))

    def test_input_set_active_invalid(self):
        """
        Checking that non-boolean update values for the input types raise Exceptions
        """
        self.assertRaises(TypeError, self._controller.get_button(InputTypes.LEFT_TRIGGER).set_active('TRU'))



if __name__ == "__main__":
    unittest.main()

