from doubly_linked_list import Doubly, Binary_Node
import unittest

class DoublyLinkedListTest(unittest.TestCase):
    def test_delete(self):
        ll = Doubly(['A', 'B', 'C'])
        ll.delete('A')
        assert ll.length_of_linked_list() == 2
        assert ll.head.data == "B"
        assert ll.is_empty() == False
        ll.delete('B')
        assert ll.is_empty() == False
        assert ll.head.data == 'C'
        assert ll.length_of_linked_list() == 1
        ll.delete('C')
        assert ll.is_empty() == True
        assert ll.length_of_linked_list() == 0
        assert ll.head == None
        assert ll.tail == None

    def test_append(self):
        ll = Doubly()
        ll.append("a")
        assert ll.length_of_linked_list() == 1
        assert ll.head.data == 'a'
        assert ll.tail.data == 'a'

        ll.append('b')
        assert ll.head.data == "a"
        assert ll.tail.data == 'b'
        assert ll.length_of_linked_list() == 2

        ll.append('c')
        assert ll.head.data == 'a'
        assert ll.tail.data == 'c'
        assert ll.length_of_linked_list() == 3

    def test_prepend(self):
        ll = Doubly
        ll.prepend('a')
        assert ll.