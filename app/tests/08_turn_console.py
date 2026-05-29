"""
Unit testing for practices
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import unittest
import app.practices.p08_turn_console as p08_turn_console

class TestTurnConsole(unittest.TestCase):
    def test_my_method(self):
        self.assertEqual(p08_turn_console.my_method(), 'My method')


if __name__ == '__main__':
    unittest.main()
