import unittest
from app.core import Word, word_distance


class WordTest(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(Word('AAA'), 'AAA')
        self.assertEqual(Word('ZZZ'), Word('ZZZ'))

    def test_add(self):
        self.assertEqual(Word('AAA') + 1, 'AAB')
        self.assertEqual(Word('A') + 1, 'B')
        self.assertEqual(Word('CFR') + 1, 'CFS')
        self.assertEqual(Word('CFA') + 8, 'CFI')

    def test_add_query(self):
        self.assertEqual(Word('AAZ') + 1, 'ABA')
        self.assertEqual(Word('Z') + 1, 'AA')
        self.assertEqual(Word('ZZ') + 1, 'AAA')
        self.assertEqual(Word('CFZ') + 1, 'CGA')
        self.assertEqual(Word('CFZ') + 4, 'CGD')

    def test_sub(self):
        self.assertEqual(Word('Z') - 1, 'Y')
        self.assertEqual(Word('D') - 3, 'A')
        self.assertEqual(Word('BAA') - 1, 'AZZ')
        self.assertEqual(Word('BAZ') - 2, 'BAX')

    def test_sub_query(self):
        self.assertEqual(Word('AA') - 1, 'Z')
        self.assertEqual(Word('AAA') - 1, 'ZZ')
        self.assertEqual(Word('AAA') - 3, 'ZX')


class WordDistanceTest(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(word_distance(Word('A'), Word('B')), 1)
        self.assertEqual(word_distance(Word('Z'), Word('AA')), 1)
        self.assertEqual(word_distance(Word('AA'), Word('BA')), 26)


def run_tests():
    unittest.main()
