import unittest
from main import *

class TestStep(unittest.TestCase):
    def setUp(self):
        self.data=[[1,1,1],[1,1,1],[1,1,1]]

    def test_step_gowest(self):
        start=[1,1]
        end, coin=nextstep(start, self.data.copy(), 'W')
        self.assertEqual(end, [0,1])
        self.assertEqual(coin, 1)
        selfdata=self.data.copy()
        selfdata[1][0]=-1
        end, coin=nextstep(start,selfdata, 'W')
        self.assertEqual(end, [1,1])
        self.assertEqual(coin, 0)
        start=[0,1]
        end, coin=nextstep(start, self.data.copy(), 'W')
        self.assertEqual(end, [0,1])
        self.assertEqual(coin, 0)


    def test_step_goeast(self):
        start=[1,1]
        end, coin=nextstep(start, self.data.copy(), 'E')
        self.assertEqual(end, [2,1])
        self.assertEqual(coin, 1)
        selfdata=self.data.copy()
        start=[2,1]
        end, coin=nextstep(start, self.data.copy(), 'E')
        self.assertEqual(end, [2, 1])
        self.assertEqual(coin, 0)
        selfdata[1][2]=-1
        end, coin=nextstep(start, selfdata, 'E')
        self.assertEqual(end, [1,1])
        self.assertEqual(coin, 0)


    def test_step_gonorth(self):
        start=[1,1]
        end, coin=nextstep(start, self.data.copy(), 'N')
        self.assertEqual(end, [1,0])
        self.assertEqual(coin, 1)
        selfdata=self.data.copy()
        start=[1,0]
        end, coin=nextstep(start, self.data.copy(), 'N')
        self.assertEqual(end, [1, 0])
        self.assertEqual(coin, 0)
        selfdata[0][1]=-1
        end, coin=nextstep(start, selfdata, 'N')
        self.assertEqual(end, [1,1])
        self.assertEqual(coin, 0)

    def test_step_gonorth(self):
        start=[1,1]
        end, coin=nextstep(start,self.data.copy(), 'S')
        self.assertEqual(end, [1,2])
        self.assertEqual(coin, 1)
        selfdata=self.data.copy()
        start=[1,2]
        end, coin=nextstep(start,self.data.copy(), 'S')
        self.assertEqual(end, [1, 2])
        self.assertEqual(coin, 0)
        selfdata[2][1]=-1
        end, coin=nextstep(start, selfdata, 'S')
        self.assertEqual(end, [1,1])
        self.assertEqual(coin, 0)

if __name__ == '__main__':
    unittest.main()
