from Quadratic_Probing_Hash_Table import Quadratic_Probing_Hash_Table
import unittest

class QuadraticProbingTesting(unittest.TestCase):
    def test_init(self):
        ht = Quadratic_Probing_Hash_Table(4)
        assert len(ht.buckets) == 4
        assert ht.counter == 0
        assert ht.size == 0

    def test_hash_function(self):
        ht = Quadratic_Probing_Hash_Table()
        assert ht.hash_function('hello') == 532
        assert ht.hash_function('h e l l o') == 660
        assert ht.hash_function(2) == 2
        assert ht.hash_function(45) == 45
        with self.assertRaises(KeyError):
            assert ht.hash_function(45.74)
