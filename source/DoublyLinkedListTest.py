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