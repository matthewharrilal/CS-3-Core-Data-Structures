#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty

        return self.list.is_empty()


    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        if self.list.is_empty() == True:
            return None
        else:
            return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Push given item
        # Think about it the top of the stack is where the head is pointing at therefore the top is at index 0
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.list.is_empty() == False:
            return self.list.get_at_index(0)
        else:
            return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any
        # We want to account for the edge case if there is not items in the stack
        if self.list.is_empty() == True:
            raise ValueError
        else:
            latest_node = self.list.get_at_index(0)
            self.list.delete(latest_node)
            return latest_node

        # Now that we have checked if the stack is empty and we are raising a value error if it is what we can do is
        # now remove the tail



# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        self.size = 0
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if self.size == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return self.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item
        self.list.append(item)
        self.size += 1

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.is_empty() == True:
            return None
        return self.list[self.size - 1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any
        if self.is_empty() == True:
            return None
        latest_node = self.list[self.size - 1]
        self.list.remove(latest_node)
        self.size -= 1
        return latest_node


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
Stack = ArrayStack

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 0:
        s = Stack()
        # s = Stack(['A', 'B', 'C'])
        # s = LinkedStack(['A', 'B', 'C'])
        # print s.peek()
        # print s.length()
        print(s.is_empty())
        # print s
    else:
        print('hello')


if __name__ == '__main__':
    main()
