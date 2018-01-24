
class Quadratic_Probing_Hash_Table(object):
    def __init__(self, init_size=8):
        '''Initalize the hash table with the given initial size'''
        self.buckets = [[] for _ in range(init_size)]
        self.size = 0 # Keeps track of the key value entries in each bucket
        self.counter = 0
        for bucket in self.buckets:
            if len(bucket) != 0:
                self.counter += 1

    def hash_function(self, key):
        # Formulates hash number from given input
        list_of_ascii_values = []
        if type(key) == str:
            # Find the ascii value for key if key is of type string
            for character in key:
                list_of_ascii_values.append(ord(character))
            ascii_key_value = (sum(list_of_ascii_values))
            hash_number = (ascii_key_value + (self.counter ** 2))
            return hash_number
        elif type(key) == int:
            hash_number = (key + (self.counter ** 2))
            return hash_number
        raise KeyError

    def _bucket_index(self, key):
        # Applies formula to find index where key value entry will be assigned
        bucket_index = self.hash_function(self.hash_function(key)) % len(self.buckets)
        return bucket_index

    def return_bucket(self, key):
        index = self._bucket_index(key)
        bucket_at_index = self.buckets[index]
        return bucket_at_index

    def load_factor(self):
        # Tells us the load factor of the hash table comes into use when we have to dynamically resize the array
        load_factor = self.size / len(self.buckets) # We calculate the load factor by dividing the number of key
        # value entries by the number of buckets in the has table
        return load_factor

    def keys_and_values(self):
        '''Returns a list of all key and value pairs in the hash table'''
        all_key_value_pairs = []
        for bucket in self.buckets:
            all_key_value_pairs.extend(bucket)
        return all_key_value_pairs

    def length(self):
        '''Returns the number of key_value entries by traversing the hash tables buckets'''
        item_count = 0
        item_count += len(self.keys_and_values()) // 2
        return item_count

    def contains(self, key):
        '''Returns True if a hash table contains a given key, False if not'''

        # Find the bucket that the key is contained in
        accurate_bucket = self.return_bucket(key)

        if accurate_bucket is None:
            raise ValueError('Contains Function undefined for non existent buckets')

        if accurate_bucket[0] == key:  # The user is suppose to save values as key value pairs
            # therefore if the first value is not the key then the list does not contain that key value entry
            return True
        else:
            return False

    def get(self, key):
        '''Return the value associated with the given key or r'''
        bucket_at_index = self.return_bucket(key)

        if bucket_at_index is None:
            raise ValueError('Get function is undefined for buckets that are non existent')

        if bucket_at_index[0] == key:
            return bucket_at_index[1]
        else:  # Not found
            raise KeyError('Key does not exist')


    def set(self, key, value):
        '''Insert the given key with its associated value'''
        bucket_at_index = self.return_bucket(key)
        key_value_entry_index_store = [0 , 1]
        key_value_entry = [key, value]
        print(bucket_at_index)

        # Now that we have the bucket that the key was hashed to we have to check if the entry exists already before we
        # insert
        if len(bucket_at_index) == 0:
            bucket_at_index.extend(key_value_entry)
        elif bucket_at_index[0] == key and bucket_at_index[1] == value:
            for positional_index in key_value_entry_index_store:
                del bucket_at_index[positional_index]
            self.size -= 1
            bucket_at_index.extend(key_value_entry)
        self.size += 1

        # Now that we have done that we have to check the load factor
        if self.load_factor() > 0.75:
            pass

    def delete(self, key):
        '''Delete a key at a given value or raise key error'''
        bucket_at_index = self.return_bucket(key)
        key_value_entry_index_store = [0, 1]

        if bucket_at_index[0] == key:
            del bucket_at_index[:]
            self.size -= 1
        else:  # The key was not found
            raise KeyError

    def resize(self, new_size=None):
        '''Resizes this hashtable and rehashes all key value entries.
        Should be resized when load facotr exceeds a threshold of 0.75'''
        if new_size is None:
            new_size = len(self.buckets) * 2  # Dobule size
        elif new_size is 0:
            new_size = len(self.buckets) / 2 # Half size we do this if the buckets are barely filled then we reduce the
            # number of buckets

        key_value_entries = self.keys_and_values()

        new_size_list = [[] for _ in range(new_size)]

        self.buckets = new_size_list

        self.size = 0

        for key, value in key_value_entries:
            self.set(key, value)






