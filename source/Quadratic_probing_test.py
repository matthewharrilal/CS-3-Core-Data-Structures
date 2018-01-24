from Quadratic_Probing_Hash_Table import Quadratic_Probing_Hash_Table
import unittest

ht = Quadratic_Probing_Hash_Table()

class QuadraticProbingTesting(unittest.TestCase):
    def test_init(self):
        h_t = Quadratic_Probing_Hash_Table(4)
        assert len(h_t.buckets) == 4
        assert h_t.counter == 0
        assert h_t.size == 0

    def test_hash_function(self):
        assert ht.hash_function('hello') == 532
        assert ht.hash_function('h e l l o') == 660
        assert ht.hash_function(2) == 2
        assert ht.hash_function(45) == 45
        with self.assertRaises(KeyError):
            assert ht.hash_function(45.74)


    def test_bucket_index(self):
        assert ht._bucket_index('hello') == 4
        assert ht._bucket_index('h e l l o') == 4
        assert ht._bucket_index(2) == 2
        assert ht._bucket_index(45) == 5

    def test_keys_and_values(self):
        assert ht.keys_and_values() == []

    def test_length(self):
        assert ht.length() == 0

    def test_set(self):
        ht.set('dog', "Dogs are Awesome")
        assert ht.size == 1
        assert ht.length() == 1
        assert ht.keys_and_values() == ['dog', "Dogs are Awesome"]
        ht.set('cats', "Cats Are Awesome")
        assert ht.size == 2
        assert ht.keys_and_values() == ['dog', "Dogs are Awesome",'cats', "Cats Are Awesome"]
        assert ht.length() == 2






