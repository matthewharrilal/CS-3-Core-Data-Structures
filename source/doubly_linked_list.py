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
            current_node = current_node.next_pointer
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
                current_node = current_node.next_pointer

    def append(self, item):
        '''Appends an a node to the end of a linked list'''
        new_node = BinaryNode(item)

        # To save time complexity we first check if the list is empty
        if self.is_empty() == True:
            # If the list is empty then we want to set the head to the new node
            self.head = new_node

        else:
            # Thats why they say that doubly linked lists are easier to work with therefore what is happening is that we
            # are setting the node that comes before the new node to the tail
            new_node.previous_pointer = self.tail
            # The reason that we set the tail to the node before this node and then back again is because since we are
            # saving time by going directly to the tail we are not keeping in mind the other nodes therefore we have to in
            # a sense backtrack to the node before and keep that in memory where as opposed to when we are iterating
            # through the linked list what we can do is that we can keep all of them in memory but that wastes more time

            # And then to append to simply save time we want to go to the tail directly since we know that when appending
            # we have to add right on to the end we can go to the tail directly and set its next pointer to the next node
            self.tail.next_pointer = new_node
        # Once we set the tails NEXT pointer to the new node we then set the tail to the new node
        self.tail = new_node
        # Since we are appending increase the size by 1
        self.size += 1
