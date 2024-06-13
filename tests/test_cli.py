import unittest
import subprocess

class TestCLI(unittest.TestCase):

    def test_get_books(self):
        result = subprocess.run(['python', 'CLI.py', '--action', 'get_books'], capture_output=True, text=True)
        self.assertIn("Title:", result.stdout)

if __name__ == '__main__':
    unittest.main()
