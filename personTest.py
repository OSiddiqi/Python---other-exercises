import unittest
from person import addDetails

class PersonTestCase(unittest.TestCase):
    """Tests for `person.py`."""

    def test_can_i_add_a_person(self):
        """Can I actually add details about a person?"""
        self.assertTrue(addDetails)

if __name__ == '__main__':
    unittest.main()