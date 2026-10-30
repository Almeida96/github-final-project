import subprocess
import sys
import unittest
from decimal import Decimal

from compound_interest import calculate, compound_interest


class InterestTests(unittest.TestCase):
    def test_amount_and_interest_are_distinct(self):
        result = calculate(1000, 2, 10)
        self.assertEqual(result["amount"], Decimal("1210"))
        self.assertEqual(result["interest"], Decimal("210"))
        self.assertEqual(compound_interest(1000, 2, 10), 1210)

    def test_zero_duration_and_zero_rate(self):
        self.assertEqual(calculate(100, 0, 10)["interest"], 0)
        self.assertEqual(calculate(100, 10, 0)["interest"], 0)

    def test_decimal_inputs(self):
        self.assertEqual(calculate("0.10", 1, 10)["amount"], Decimal("0.11"))

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            compound_interest(1, 1000, 1000)
        for value in ("NaN", "Infinity", -1, True, "missing", 10**20):
            with self.subTest(value=value), self.assertRaises(ValueError):
                calculate(value, 1, 1)

    def test_cli_and_failure_exit(self):
        result = subprocess.run([sys.executable, "compound_interest.py", "--principal", "1000",
                                 "--years", "2", "--rate", "10"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("Interest: 210.00", result.stdout)
        bad = subprocess.run([sys.executable, "compound_interest.py", "--principal", "nan",
                              "--years", "2", "--rate", "10"], capture_output=True, text=True)
        self.assertEqual(bad.returncode, 2)
