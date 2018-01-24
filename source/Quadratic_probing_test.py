from Quadratic_Probing_Hash_Table import Quadratic_Probing_Hash_Table
import unittest

class QuadraticProbingTesting(unittest.TestCase):
    def test_init(self):
        ht = Quadratic_Probing_Hash_Table(4)
        assert len(ht.buckets) == 4
        assert ht.counter == 0
        assert ht.size == 0