import unittest
from wordsoup import wordsoup, txt_read

class TestStringMethods(unittest.TestCase):
    # test function to test equality of two value
    def test_wordsoup(self):
        fname = "Read.txt"
        message = "Values are not unequal!"
        self.assertNotEqual(txt_read(fname), wordsoup(fname), message)
  
if __name__ == '__main__':
    unittest.main()
