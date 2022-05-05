import unittest

import mc


class TestMarkov(unittest.TestCase):
    def test_get_table(self):
        res = mc.get_table('ab')
        self.assertEqual(res, {'a': {'b': 1}})

    def test_get_table2(self):
        res = mc.get_table('abc', size=2)
        self.assertEqual(res, {'ab': {'c': 1}})

    def test_predict(self):
        m = mc.Markov('ab')
        res = m.predict('a')
        self.assertEqual(res, 'b')

    def test_predict2(self):
        m = mc.Markov('abc', size=2)
        res = m.predict('a')
        self.assertEqual(res, 'b')
        res = m.predict('ab')
        self.assertEqual(res, 'c')


if __name__ == '__main__':
    unittest.main()
else:
    print('loading as library')