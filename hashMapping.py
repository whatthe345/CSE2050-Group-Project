class HashMapping:
    def __init__(self,size=2) :
        self.size = size
        self.hash_table = [[] for _ in range(size)]
    def _find_bucket(self, item):
        """Returns the index of the bucket `item` should go in, based on hash(item) and self.n_buckets"""
        # hash(item) returns a nice "random" integer using item.__hash__()
        # Use % to scale that hash to a number between 0 and n_buckets
        return hash(item) % self.size
    def put(self,key,value):
        """adds an entry to a hash table given a value and key"""
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                bucket[index] = (key, value)
            return
        bucket.append((key, value))
    def get(self,key):
        """gets the value associated with a key from a hash table"""
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        for record_key, record_val in bucket:
            if record_key == key:
                return record_val
        raise KeyError
    def __contains__(self,key):
        """returns true or false if the key is in the hash table"""
        if self.get(key) is ValueError:
            return False
        else:
            return True
    def __len__(self):
        """returns the length of a hash table"""
        return len(self.hash_table)
    def rehash(self):
        """Rehashes every item from a hash table with n_buckets to one with new_buckets. new_buckets will be either 2*n_buckets or 1/2*n_buckets, depending on whether we are reahshing up or down."""
        # Make a new list of `new_buckets` empty lists
        self.size = self.size * 2
        new_li=[[] for i in range(self.size)]

        # Using a for loop, iterate over every bucket in self._L
            # using a for loop, iterate over every item in this bucket
                # Find the index of the new bucket for that item
                # add that item to the correct bucket
        for bucket in self.hash_table:
            for item in bucket:
                new_idx = self._find_bucket(item)
                new_li[new_idx].append(item)
        # Update self._L to point to the new list
        self.hash_table=new_li