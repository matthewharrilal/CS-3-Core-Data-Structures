
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
        bucket_index = self.hash_function(self.hash_function(key)) % len(self.buckets)
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

        # Find the bucket that the key is contained in
        index_of_bucket = self._bucket_index(key)
        accurate_bucket = self.buckets[index_of_bucket]

        if accurate_bucket is None:
            raise ValueError('Contains Function undefined for non existent buckets')

        if accurate_bucket[0] == key:  # The user is suppose to save values as key value pairs
            # therefore if the first value is not the key then the list does not contain that key value entry
            return True
        return False

    def get(self, key):
        '''Return the value associated with the given key or r'''
        index_of_bucket = self._bucket_index(key)  # Getting the index of the bucket
        bucket_at_index = self.buckets[index_of_bucket]

        if bucket_at_index is None:
            raise ValueError('Get function is undefined for buckets that are non existent')

        if bucket_at_index[0] == key:
            return bucket_at_index[1]
        else:  # Not found
            raise KeyError('Key does not exist')


    def set(self, key, value):
        '''Insert the given key with its associated value'''
        index = self._bucket_index(key)
        bucket_at_index = self.buckets[index]
        key_value_entry_index_store = [0 , 1]
        key_value_entry = [key, value]

        # Now that we have the bucket that the key was hashed to we have to check if the entry exists already before we
        # insert
        if bucket_at_index[0] == key and bucket_at_index[1] == value:
            for positional_index in key_value_entry_index_store:
                del bucket_at_index[positional_index]
            self.size -= 1
        bucket_at_index.extend(key_value_entry)
        self.size += 1

        # Now that we have done that we have to check the load factor
        if self.load_factor() > 0.75:
            pass






