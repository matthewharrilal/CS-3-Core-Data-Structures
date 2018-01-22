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

    def items(self):
        '''Return a list of all items in the linked list'''
        # This will not be different from the regular linked list because there is no need for the previous property
        current_node = self.head
        result_list = [] # Have a empty list so that we can contain all the nodes that we have iterated upon

        while current_node is not None:
            result_list.append(current_node.data)

            # We do this step so that we can continue iterating through the list
            current_node = current_node.next
        return result_list

    def is_empty(self):
        '''Returns a boolean value indicating whether or not our linked list is empty or not'''
        if self.size == 0:
            return True
        return False

    def length_of_linked_list(self):
        return self.size

    def get_at_index(self, index):
        '''Return item at given index or raise Value Error if list index is out of range or return None if list is empty'''

        # Checks if the index is out of range of the linked list
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        # Checks if the linked list is empty if so returns None
        if self.is_empty() == True:
            return None
        else:
            current_node = self.head
            counter = 0
            if counter == index:
                return current_node.data

            while current_node is not None:
                if counter == index:
                    return current_node.data
                counter += 1
                current_node = current_node.next
