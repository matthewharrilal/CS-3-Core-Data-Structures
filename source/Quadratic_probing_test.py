from Quadratic_Probing_Hash_Table import Quadratic_Probing_Hash_Table
import unittest


class QuadraticProbingTesting(unittest.TestCase):
    def test_init(self):
        h_t = Quadratic_Probing_Hash_Table(4)
        assert len(h_t.buckets) == 4
        assert h_t.counter == 0
        assert h_t.size == 0

    def test_hash_function(self):
        ht = Quadratic_Probing_Hash_Table()

        assert ht.hash_function('hello') == 532
        assert ht.hash_function('h e l l o') == 660
        assert ht.hash_function(2) == 2
        assert ht.hash_function(45) == 45
        with self.assertRaises(KeyError):
            assert ht.hash_function(45.74)


    def test_bucket_index(self):
        ht = Quadratic_Probing_Hash_Table()
        assert ht._bucket_index('hello') == 4
        assert ht._bucket_index('h e l l o') == 4
        assert ht._bucket_index(2) == 2
        assert ht._bucket_index(45) == 5

    def test_set(self):
        ht = Quadratic_Probing_Hash_Table()
        ht.set('dog', "Dogs are Awesome")
        assert ht.size == 1
        assert ht.length() == 1
        assert ht.keys_and_values() == ['dog', "Dogs are Awesome"]
        ht.set('cats', "Cats Are Awesome")
        assert ht.size == 2
        assert ht.keys_and_values() == ['dog', "Dogs are Awesome",'cats', "Cats Are Awesome"]
        assert ht.length() == 2


    def test_length_and_set(self):
        ht = Quadratic_Probing_Hash_Table()
        assert ht.length() == 0
        assert ht.size == 0
        ht.set('Matthew', "Matthew Harrilal is the name")
        assert ht.length() == 1
        assert ht.size == 1
        ht.set('Nerd', "Duncan is a nerd")
        ht.set('Nest Labs', "Nest Hire Me")
        assert ht.length() == 3
        assert ht.size == 3

    def test_keys_and_values_and_set(self):
        h__t = Quadratic_Probing_Hash_Table()
        h__t.set("Matthew", "Matthew is the coolest cat on the playground")
        assert h__t.length() == 1
        assert h__t.size == 1
        assert h__t.keys_and_values() == ["Matthew", "Matthew is the coolest cat on the playground"]
        h__t.set('Nest Labs', "Nest Labs Please Hire Me")
        assert h__t.length() == 2
        assert  h__t.size == 2
        assert  h__t.keys_and_values() == ["Matthew", "Matthew is the coolest cat on the playground", 'Nest Labs', "Nest Labs Please Hire Me"]


    def test_contains(self):
        ht = Quadratic_Probing_Hash_Table()
        ht.set('Mom', "Mom I love you")
        assert ht.size == 1
        assert ht.contains('Mom') == True
        assert ht.length() == 1
        assert ht.keys_and_values() == ['Mom', "Mom I love you"]
        ht.set('Dad', "Dad I love you")




