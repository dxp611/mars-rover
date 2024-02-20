import unittest
from main import run

class Testing(unittest.TestCase):
  def test_1(self):
    input = [4, 8, ((2, 3, 'E'), 'LFRFF'), ((0, 2, 'N'), 'FFLFRFF')]
    expected = ['(4, 4, E)', '(0, 4, W) LOST']
    
    self.assertEqual(run(input), expected)

  def test_2(self):
    input = [4, 8, ((2, 3, 'N'), 'FLLFR'), ((1, 0, 'S'), 'FFRLF')]
    expected = ['(2, 3, W)', '(1, 0, S) LOST']
    self.assertEqual(run(input), expected)

if __name__ == '__main__':
  unittest.main()