
class Quadratic_Probing_Hash_Table(object):
    def __init__(self, init_size=8):
        '''Initalize the hash table with the given initial size'''
        self.buckets = [[] for _ in range(init_size)]
        self.size = 0 # Keeps track of the key value entries in each bucket

    def hash_function(self, key, counter=0):
        # Formulates hash number from given input
        if type(key) != str or type(key) != int:
            raise ValueError('Hash function undefined for key type other than string or integer')
        list_of_ascii_values = []
        if type(key) == str:
            # Find the ascii value for key if key is of type string
            for character in key:
                list_of_ascii_values.append(ord(character))
            ascii_key_value = int(''.join(sum(list_of_ascii_values)))
            hash_number = (ascii_key_value + (counter ** 2)) % len(self.buckets)
            return hash_number
        else:
            hash_number = (key + (counter ** 2)) % len(self.buckets)
            return hash_number


    def bucket_index(self, key):
        # Applies formula to find index where key value entry will be assigned
        bucket_index = self.hash_function(key) % len(self.buckets)
        return bucket_index

    def load_factor(self):
        # Tells us