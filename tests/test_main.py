import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertIsNone(main())  # Main function should complete without errors

if __name__ == "__main__":
    unittest.main()
