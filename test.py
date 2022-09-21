import unittest
from preprocess import read_text

class MainTestCase(unittest.TestCase):    
    def io_test(self):
        self.assertEqual('Our team had a debate for best names for looping variables ? i won', read_text('text_files/test.txt'))

if __name__ == '__main__':
    unittest.main()
