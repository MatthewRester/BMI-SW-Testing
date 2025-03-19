import unittest
from BMI_Calculator import calculate_bmi, categorize_bmi

class TestBMICalculator(unittest.TestCase):

    # This tests the calculate_bmi function to ensure it calculates correctly.
    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(69, 160), 23.6, places=1)  # 5'9", 160 lbs
        self.assertAlmostEqual(calculate_bmi(72, 200), 27.1, places=1)  # 6'0", 200 lbs
        self.assertAlmostEqual(calculate_bmi(60, 100), 19.5, places=1)  # 5'0", 100 lbs

    # This tests the categorize_bmi function to ensure is maps bmi's correctly.
    def test_bmi_categorization(self):
        self.assertEqual(categorize_bmi(18.4), "Underweight")
        self.assertEqual(categorize_bmi(18.5), "Normal weight")
        self.assertEqual(categorize_bmi(24.9), "Normal weight")
        self.assertEqual(categorize_bmi(25.0), "Overweight")
        self.assertEqual(categorize_bmi(29.9), "Overweight")
        self.assertEqual(categorize_bmi(30.0), "Obese")

    # This tests the potential erros thrown when an invalid (<=0) height or weight is entered.
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculate_bmi(0, 170)
        with self.assertRaises(ValueError):
            calculate_bmi(65, 0)
        with self.assertRaises(ValueError):
            calculate_bmi(-65, 170)
        with self.assertRaises(ValueError):
            calculate_bmi(65, -170)

if __name__ == '__main__':
    unittest.main()