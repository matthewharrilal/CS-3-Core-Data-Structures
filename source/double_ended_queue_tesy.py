from queue import Queue
import unittest

class QueueTest(unittest.TestCase):
    def test_init(self):
        q = Queue()
        assert q.front() is None
        assert q.length() == 0
        assert q.is_empty() is True

    def test_init_with_list(self):
        q = Queue(['A', 'B', 'C'])
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False


    def test_length(self):
        q = Queue()
        assert q.length() == 0
        q.enqueue_left('A')
        assert q.length() == 1
        q.enqueue_left('B')
        assert q.length() == 2
        q.delete_right()
        assert q.length() == 1
        q.delete_right()
        assert q.length() == 0
    #
    def test_enqueue_left(self):
        q = Queue()
        q.enqueue_left('A')
        assert q.front() == 'A'
        assert q.length() == 1
        q.enqueue_left('B')
        assert q.front() == 'B'
        assert q.length() == 2
        q.enqueue_left('C')
        assert q.front() == 'C'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_front(self):
        q = Queue()
        assert q.front() is None
        q.enqueue_left('A')
        assert q.front() == 'A'
        q.enqueue_left('B')
        assert q.front() == 'B'
        q.delete_right()
        assert q.front() == 'B'
        q.delete_right()
        assert q.front() is None

    def test_delete_right(self):
        q = Queue(['A', 'B', 'C'])
        assert q.delete_right() == 'C'
        assert q.length() == 2
        assert q.delete_right() == 'B'
        assert q.length() == 1
        assert q.delete_right() == 'A'
        assert q.length() == 0
        assert q.is_empty() is True
        with self.assertRaises(ValueError):
            q.delete_right()

    def test_enqueue_right(self):
        q = Queue()
        assert q.front() == None
        q.enqueue_right('A')
        assert q.length() == 1
        assert q.front() == 'A'
        q.enqueue_right('B')
        assert q.length() == 2
        assert q.front() == "A"
        q.enqueue_right('C')
        assert  q.length() == 3
        assert  q.front() == "A"

    def test_delete_left(self):
        q = Queue(['A', 'B', 'C'])
        assert q.length() == 3
        assert  q.front() == 'A'
        assert q.delete_left() == 'A'
        assert q.length() == 2
        assert q.front() == "B"
        assert q.delete_left() == 'B'
        assert q.front() == "C"
        assert q.length() == 1
        assert q.delete_left() == "C"
        assert q.front() == None
        assert q.length() == 0
        assert  q.is_empty() == True

    def test_is_empty(self):
        q = Queue()
        assert q.is_empty() == True
        assert q.length() == 0
        q.enqueue_left('A')
        assert q.is_empty() == False

