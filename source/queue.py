#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return self.list.size


    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item
        self.list.append(item)


    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.list.is_empty() == True:
            return None
        top_node = self.list.get_at_index(0)
        return top_node

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return front item, if any
        if self.list.is_empty() == True:
            raise ValueError
        front_node = self.list.get_at_index(0)
        self.list.delete(front_node)
        return front_node

class DoubleEndedQueue(object):
    def __init__(self, iterable=None):
        '''Initialize the given function for a deqeue'''
        self.list = list()
        self.size = 0
        if iterable is not None:
            for item in iterable:
                # The reason we want to enqueue from the right is because that is the natural way we append to an array
                self.enqueue_right(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def length(self):
        return self.size

    def enqueue_left(self, item):
        self.list.insert(0, item)
        self.size += 1

    def enqueue_right(self, item):
        self.list.append(item)
        self.size += 1

    def delete_left(self):
        '''Removes and return leftmost element which is the first node '''
        if self.is_empty() == True:
            raise ValueError
        first_node = self.list[0]
        self.list.remove(first_node)
        self.size -= 1
        return first_node

    def delete_right(self):
        if self.is_empty() == True:
            raise ValueError
        latest_node = self.list[self.size - 1]
        self.list.remove(latest_node)
        self.size -= 1
        return latest_node

    def front(self):
        if self.is_empty() == True:
            return None
        front_node = self.list[0]
        print('This is the front %s' % (self.list[self.size - 1]))
        return front_node




# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        # Want to keep track of the size of this array in linear time
        self.size = 0
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        if self.size == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return self.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item
        self.list.append(item)
        self.size += 1


    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.is_empty() == True:
            return None
        front_node = self.list[0]
        return front_node


    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return front item, if any
        if self.is_empty() == True:
            raise ValueError
        front_node = self.list[0]
        self.list.remove(front_node)
        self.size -= 1
        return front_node

# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
# Queue = ArrayQueue
Queue = DoubleEndedQueue

