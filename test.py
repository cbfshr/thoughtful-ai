import unittest
import robotic_automation_factory

class TestSortMethods(unittest.TestCase):

    def test_standard(self):
        self.assertEqual(robotic_automation_factory.PACKAGE_STANDARD, robotic_automation_factory.sort(1, 2, 3, 4))
        # Almost Bulky
        self.assertEqual(robotic_automation_factory.PACKAGE_STANDARD, robotic_automation_factory.sort(149.99, 2, 3, 4))
        self.assertEqual(robotic_automation_factory.PACKAGE_STANDARD, robotic_automation_factory.sort(1, 149.99, 3, 4))
        self.assertEqual(robotic_automation_factory.PACKAGE_STANDARD, robotic_automation_factory.sort(1, 2, 149.99, 4))
        self.assertEqual(robotic_automation_factory.PACKAGE_STANDARD, robotic_automation_factory.sort(100, 100, 99.9999, 4))
        # Almost Heavy
        self.assertEqual(robotic_automation_factory.PACKAGE_STANDARD, robotic_automation_factory.sort(1, 2, 3, 19.99))

    def test_special(self):
        # Bulky - Width
        self.assertEqual(robotic_automation_factory.PACKAGE_SPECIAL, robotic_automation_factory.sort(150, 2, 3, 4))
        self.assertEqual(robotic_automation_factory.PACKAGE_SPECIAL, robotic_automation_factory.sort(150.1, 2, 3, 4))
        self.assertEqual(robotic_automation_factory.PACKAGE_SPECIAL, robotic_automation_factory.sort(151, 2, 3, 4))
        # Bulky - Height
        self.assertEqual(robotic_automation_factory.PACKAGE_SPECIAL, robotic_automation_factory.sort(1, 150, 3, 4))
        self.assertEqual(robotic_automation_factory.PACKAGE_SPECIAL, robotic_automation_factory.sort(1, 150.1, 3, 4))
        self.assertEqual(robotic_automation_factory.PACKAGE_SPECIAL, robotic_automation_factory.sort(1, 151, 3, 4))
        self.assertEqual(robotic_automation_factory.PACKAGE_SPECIAL, robotic_automation_factory.sort(1, 402, 3, 4))
        # Bulky - Length
        self.assertEqual(robotic_automation_factory.PACKAGE_SPECIAL, robotic_automation_factory.sort(55, 2, 150, 4))
        self.assertEqual(robotic_automation_factory.PACKAGE_SPECIAL, robotic_automation_factory.sort(55, 2, 150.1, 4))
        self.assertEqual(robotic_automation_factory.PACKAGE_SPECIAL, robotic_automation_factory.sort(55, 2, 151, 4))
        self.assertEqual(robotic_automation_factory.PACKAGE_SPECIAL, robotic_automation_factory.sort(55, 2, 5000, 4))
        # Bulky - Volume
        self.assertEqual(robotic_automation_factory.PACKAGE_SPECIAL, robotic_automation_factory.sort(100, 100, 100, 15))
        self.assertEqual(robotic_automation_factory.PACKAGE_SPECIAL, robotic_automation_factory.sort(100, 100, 101, 15))
        # Heavy
        self.assertEqual(robotic_automation_factory.PACKAGE_SPECIAL, robotic_automation_factory.sort(1, 2, 3, 20))
        self.assertEqual(robotic_automation_factory.PACKAGE_SPECIAL, robotic_automation_factory.sort(1, 2, 3, 21))
        
    def test_rejected(self):
        self.assertEqual(robotic_automation_factory.PACKAGE_REJECTED, robotic_automation_factory.sort(150, 2, 3, 20))
        self.assertEqual(robotic_automation_factory.PACKAGE_REJECTED, robotic_automation_factory.sort(151, 2, 3, 21))
        self.assertEqual(robotic_automation_factory.PACKAGE_REJECTED, robotic_automation_factory.sort(100, 100, 100, 20))
        self.assertEqual(robotic_automation_factory.PACKAGE_REJECTED, robotic_automation_factory.sort(100, 100, 101, 21))

    def test_edge_cases(self):
        with self.assertRaises(Exception) as e:
            robotic_automation_factory.sort(-1, 2, 3, 20)
        self.assertEqual("Width, Height, and Length cannot be less than or equal to 0.", str(e.exception))
        with self.assertRaises(Exception) as e:
            robotic_automation_factory.sort(1, -1, 3, 20)
        self.assertEqual("Width, Height, and Length cannot be less than or equal to 0.", str(e.exception))
        with self.assertRaises(Exception) as e:
            robotic_automation_factory.sort(1, 2, -3, 20)
        self.assertEqual("Width, Height, and Length cannot be less than or equal to 0.", str(e.exception))
        with self.assertRaises(Exception) as e:
            robotic_automation_factory.sort(1, 2, 3, -1)
        self.assertEqual("Mass cannot be less than or equal to 0.", str(e.exception))
        with self.assertRaises(Exception) as e:
            robotic_automation_factory.sort("1", 2, 3, 1)
        self.assertEqual("Width, Height, and Length must be numbers.", str(e.exception))
        with self.assertRaises(Exception) as e:
            robotic_automation_factory.sort("one", 2, 3, 1)
        self.assertEqual("Width, Height, and Length must be numbers.", str(e.exception))
        with self.assertRaises(Exception) as e:
            robotic_automation_factory.sort(1, "3", 3, 1)
        self.assertEqual("Width, Height, and Length must be numbers.", str(e.exception))
        with self.assertRaises(Exception) as e:
            robotic_automation_factory.sort(1, "three", 3, 1)
        self.assertEqual("Width, Height, and Length must be numbers.", str(e.exception))
        with self.assertRaises(Exception) as e:
            robotic_automation_factory.sort(1, 3, "3", 1)
        self.assertEqual("Width, Height, and Length must be numbers.", str(e.exception))
        with self.assertRaises(Exception) as e:
            robotic_automation_factory.sort(1, 3, "three", 1)
        self.assertEqual("Width, Height, and Length must be numbers.", str(e.exception))
        with self.assertRaises(Exception) as e:
            robotic_automation_factory.sort(1, 3, 6, "19")
        self.assertEqual("Mass must be a number.", str(e.exception))
        with self.assertRaises(Exception) as e:
            robotic_automation_factory.sort(None, 5, 8, 1)
        self.assertEqual("Width, Height, and Length must be numbers.", str(e.exception))
        with self.assertRaises(Exception) as e:
            robotic_automation_factory.sort(1, None, 2, 1)
        self.assertEqual("Width, Height, and Length must be numbers.", str(e.exception))
        with self.assertRaises(Exception) as e:
            robotic_automation_factory.sort(1, 5, None, 1)
        self.assertEqual("Width, Height, and Length must be numbers.", str(e.exception))
        with self.assertRaises(Exception) as e:
            robotic_automation_factory.sort(1, 5, 1, None)
        self.assertEqual("Mass must be a number.", str(e.exception))

if __name__ == '__main__':
    unittest.main()
