import unittest
import preprocess as p
from wordsoup import wordsoup, txt_read

class MainTestCase(unittest.TestCase):    
    def io_test(self):
        self.assertEqual('Our team had a debate for best names for looping variables ? i won', p.read_text('text_files/test.txt'))

    def test_text_proc_replace_contractions(self):
        test_string = "Hi   \nHow're\nYou?\nI'm well!\n Don't? Would've, I'll, she's, she'll!\n"
        expected_string_no_conts = "hi how are you i am well do not would have i will she is she will"
        self.assertEqual(expected_string_no_conts, p.preproc_str(test_string, replaceContractions=True))

    def test_text_proc_with_contractions(self):
        test_string = "Hi   \nHow're\nYou?\nI'm well!\n Don't? Would've, I'll, she's, she'll!\n"
        expected_string_with_conts = "hi howre you im well dont wouldve ill shes shell"
        self.assertEqual(expected_string_with_conts, p.preproc_str(test_string, replaceContractions=False))

    def test_text_proc_joke(self):
        test_string = "Our team had a debate for best names for looping variables ? i won"
        expected_string = "our team had a debate for best names for looping variables i won"
        self.assertEqual(expected_string, p.preproc_str(test_string))

    def test_word_count(self):
        test_string = "Our team had a debate for best names for looping variables ? i won"
        expected_count = 13
        self.assertEqual(expected_count, p.get_word_count(test_string))
    # test function to test equality of two value
    def test_wordsoup(self):
        fname = "Read.txt"
        message = "Values are not unequal!"
        self.assertNotEqual(txt_read(fname), wordsoup(fname), message)

if __name__ == '__main__':
    unittest.main()
