
class Quadratic_Probing_Hash_Table(object):
    def __init__(self, init_size=8):
        '''Initalize the hash table with the given initial size'''
        self.buckets = [[] for _ in range(init_size)]
        self.size = 0 # Keeps track of the key value entries in each bucket
        self.counter = 0

    def hash_function(self, key):
        # Formulates hash number from given input
        if type(key) != str or type(key) != int:
            raise ValueError('Hash function undefined for key type other than string or integer')
        list_of_ascii_values = []
        if type(key) == str:
            # Find the ascii value for key if key is of type string
            for character in key:
                list_of_ascii_values.append(ord(character))
            ascii_key_value = int(''.join(sum(list_of_ascii_values)))
            hash_number = (ascii_key_value + (self.counter ** 2)) % len(self.buckets)
            return hash_number
        else:
            hash_number = (key + (self.counter ** 2)) % len(self.buckets)
            return hash_number


    def _bucket_index(self, key):
        # Applies formula to find index where key value entry will be assigned
        bucket_index = self.hash_function(key) % len(self.buckets)
        return bucket_index

    def load_factor(self):
        # Tells us the load factor of the hash table comes into use when we have to dynamically resize the array
        load_factor = self.size / len(self.buckets) # We calculate the load factor by dividing the number of key
        # value entries by the number of buckets in the has table
        return load_factor

    def keys_and_values(self):
        '''Returns a list of all key and value pairs in the hash table'''
        all_key_value_pairs = []
        for bucket in self.buckets:
            for key_value_pair in bucket:
                all_key_value_pairs.extend(key_value_pair)
        return all_key_value_pairs

    def length(self):
        '''Returns the number of key_value entries by traversing the hash tables buckets'''
        item_count = 0
        for key_value_entry in self.keys_and_values():
            item_count += key_value_entry
        return item_count

    def contains(self, key):
        '''Returns True if a hash table contains a given key, False if not'''
        # We can check our most basic edge case and that is if the list is empty
        if len(self.buckets) == 0 or:
            return False

        # Find the bucket that the key is contained in
        hashed_key = self.hash_function(key)
        index_of_bucket = self._bucket_index(hashed_key)
        accurate_bucket = self.buckets[index_of_bucket]

        for entry in accurate_bucket:
            if hashed_key == entry:
                return True
        return False



