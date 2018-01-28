from Sets import Set
import unittest

class Set_Test(unittest.TestCase):
    def test_init(self):
        set_instance = Set()
        assert set_instance.size == 0
        assert set_instance.hash_table.size == 0

    def test_add_element(self):
        "Have to instantiate the set with 1 or more because initally the hash table has zero buckets"
        instance_set = Set(4)
        assert instance_set.size == 0
        instance_set.add_element("Matthew")
        assert instance_set.size == 1
        instance_set.add_element("Test")
        assert instance_set.size == 2

    def test_contains(self):
        instance_set = Set(4)
        instance_set.add_element("test")
        instance_set.add_element("matthew")
        assert instance_set.size == 2
        assert instance_set.contains("matthew") == True
        assert instance_set.contains('test') == True
        assert instance_set.contains('random') == False

    def test_remove_element(self):
        instance_set = Set(4)
        instance_set.add_element('matthew')
        instance_set.add_element('harrilal')
        assert instance_set.size == 2
        instance_set.remove_element('matthew')
        assert instance_set.contains('matthew') == False
        assert instance_set.size == 1
        assert instance_set.contains('harrilal') == True
        instance_set.remove_element('harrilal')
        assert instance_set.size == 0
        assert instance_set.contains('harrilal') == False
        assert instance_set.contains('matthew') == False

    def test_union(self):
        first_set = Set(4)
        second_set = Set(4)
        first_set.add_element('matthew')
        first_set.add_element('castro')
        second_set.add_element('programmers')
        union_set = first_set.union(second_set)
        assert union_set.contains('matthew') == True
        assert union_set.contains('castro') == True
        assert union_set.contains("programmers") == True

    def test_intersection(self):
        first_set = Set(4)
        second_set = Set(4)
        first_set.add_element("Matthew")
        first_set.add_element("Castro")
        first_set.add_element("Harrilal")
        second_set.add_element("Corey")
        second_set.add_element("Castro")
        assert first_set.size == 3
        assert second_set.size == 2
        intersection_set = first_set.intersection(second_set)
        assert intersection_set.contains("Matthew") == True
        assert intersection_set.contains("Castro") == False
        assert intersection_set.contains("Harrilal") == True



