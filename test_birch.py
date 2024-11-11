import unittest
from birch import Birch

class TestBirch(unittest.TestCase):
    def test_initialization(self):
        birch = Birch(threshold=0.3, branching_factor=40)
        self.assertEqual(birch.threshold, 0.3)
        self.assertEqual(birch.branching_factor, 40)
    
    # Dodaj kolejne testy dla innych funkcji w przyszłości

if __name__ == "__main__":
    unittest.main()
