class BinaryNode(object):
    def __init__(self, data):
        '''Initalize the binary node with the given data'''
        self.previous_pointer=None
        self.data = data
        self.next_pointer=None

    def __repr__(self):
        '''Return a string representation of this node'''
        return 'Node({!r})'.format(self.data)



class DoublyLinkedList(object):
    def __init__(self, iterable=None):
        '''Initalize this linked list and append given items if any'''
        self.head = None
        self.tail = None
        self.size = 0 # The amount of nodes in the doubly linked list
        if iterable is not None:
            for item in iterable:
                self.append(item)


    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())
