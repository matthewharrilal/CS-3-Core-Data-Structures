from hashtable import HashTable

class Set(object):
    def __init__(self, elements=0):
        # We are implementing a set using the hash tables as a backing therefore we implement the hash table with the
        # number of elements that the user is given
        self.hash_table = HashTable(elements)
        self.size = 0

    def contains(self, element):
        return self.hash_table.contains(element)

    def add_element(self, element):
        element_existence_value = self.contains(element)
        added_element = self.hash_table.set(element, element_existence_value)
        self.size += 1
        return added_element

    def remove_element(self, element):
        if self.contains(element) == False:
            raise KeyError
        else:
            self.hash_table.delete(element)
        # Making tests for something that does not return anything
        self.size -= 1

    def get_keys(self):
        return self.hash_table.keys()

    def union(self, other_set):
        '''Returns a new set that is the union of this set and the other set'''
        # temp_set = self.hash_table
        # union_set = self.hash_table
        # for self_element in other_set.get_keys():
        #     if not union_set.contains(self_element):
        #         union_set.add_element(self_element)
        # self.hash_table = temp_set
        # return union_set

        union_set = Set(4)

        for self_element in self.hash_table.keys():
            union_set.add_element(self_element)

        for other_set_element in other_set.get_keys():
            union_set.add_element(other_set_element)

        return union_set


    def intersection(self,other_set):
        '''Returns a new set that is a intersection of this set and the other set '''
        intersection_set = Set(4)

        for element in self.get_keys():
            if other_set.contains(element):
                intersection_set.add_element(element)
        return intersection_set

    def difference(self, other_set):
        '''Returns a new set that is the difference of this set and the other set'''
        difference_set = Set(4)

        # Iterating through the elements in the hash table and the elements in the second set and checking if the
        # second set contains any elements that the first set has
        for element in self.get_keys():
            if element not in other_set.get_keys():
                # Whatever elements in set A that are not in set B then we append those elements
                difference_set.add_element(element)
        return difference_set

    def subset(self, other_set):
        '''Return a boolean value indicating whether other set is a subset of this set'''
        if len(self.get_keys()) > len(other_set.get_keys()):
            return False

        for element in other_set.get_keys():
            if self.contains(element):
                # This allows us to continue the iteration even after the condition is satisfied
                # But the reason we need to do this is due to the reason even if we are iterating through using a for
                # loop we have to return a boolean value therefore the first match will cause a return so we continue
                continue
            else:
                return False
        return True
if __name__ == '__main__':
    test_set = Set(5)
    test_set.add_element('key')
    print(test_set.get_keys())



