from hashtable import HashTable

class Set(object):
    def __init__(self, elements=None):
        # We are implementing a set using the hash tables as a backing therefore we implement the hash table with the
        # number of elements that the user is given
        self.hash_table = HashTable(elements)
        self.size = 0

    def contains(self, element):
        return self.hash_table.contains(element)

    def add_element(self, element):
        element_existence_value = self.contains(element)
        added_element = self.hash_table.set(element, element_existence_value)
        return added_element

    def remove_element(self, element):
        if self.contains(element) == False:
            raise KeyError
        else:
            self.hash_table.delete(element)





