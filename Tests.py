import unittest
import Reader
from Building import Building
import pandas as pd
import os

class Test(unittest.TestCase):
    def test_B3_B4_B5(self):
        b = ["B3.json", "B4.json", "B5.json"]
        c = ["Calls_a.csv", "Calls_b.csv", "Calls_c.csv", "Calls_d.csv"]
        ind = 2
        for i in b:
            for j in c:
                Reader.read_calculate_write(i, j, f'output{ind}')
                file = pd.read_csv(f'output{ind}', header=None)
                ind += 1
                for k in file[[5]].value_counts():
                    # each elev should have at least 10 calls
                    self.assertTrue(k > 10)
        for i in range(2,14):
            if os.path.exists(f'output{i}'):
                os.remove(f'output{i}')
            else:
                print(f'The file output{i} does not exist')

    def test_B1_B2(self):

        ind = 0
        Reader.read_calculate_write("B1.json", "Calls_a.csv", f'output{ind}')
        file = pd.read_csv(f'output{ind}', header=None)
        ind += 1
        #first elev should have all the calls because there is only 1 elevator
        self.assertTrue(file[[5]].value_counts()[0] >= len(file.index))
        Reader.read_calculate_write("B2.json", "Calls_a.csv", f'output{ind}')
        file = pd.read_csv(f'output{ind}', header=None)
        self.assertTrue(file[[5]].value_counts()[0] >= len(file.index) * 0.3)
        #fast elev should get most of the calls
        self.assertTrue(file[[5]].value_counts()[1] >= len(file.index) * 0.6)
        # delete files
        for i in range(2):
            if os.path.exists(f'output{i}'):
                os.remove(f'output{i}')
            else:
                print(f'The file output{i} does not exist')


if __name__ == '__main__':
    unittest.main()
