import unittest
from main import *

class TestStep(unittest.TestCase):
    def setUp(self):
        self.data=[[1,1,1],[1,1,1],[1,1,1]]

    def test_step_gowest(self):
        start=[1,1]
        end, coin=nextstep(start,self.data.copy(), 'W')
        self.assertEqual(end, [0,1])
        self.assertEqual(coin, 1)
        selfdata=self.data.copy()
        selfdata[1][0]=-1
        end, coin=nextstep(start,self.data.copy(), 'W')
        self.assertEqual(end, [1,1])
        self.assertEqual(coin, 0)
        start=[0,1]
        end, coin=nextstep(start,self.data.copy(), 'W')
        self.assertEqual(end, [0,1])
        self.assertEqual(coin, 0)

if __name__ == '__main__':
    unittest.main()
