class HashMapping:
    def __init__(self,size=2) :
        self.size = size
        self.hash_table = [[] for _ in range(size)]
        self.count = 0  # number of stored entries
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
        self.count += 1
        if self.count > self.size * 2: self.rehash()
    def get(self,key):
        """gets the value associated with a key from a hash table"""
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        for record_key, record_val in bucket:
            if record_key == key:
                return record_val
        raise KeyError
    def __contains__(self, key):
        """Returns True if the key is in the table, otherwise False."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    def __len__(self):
        """Returns the number of entries stored in the table."""
        return self.count
    def rehash(self):
        """Doubles the number of buckets and re-inserts every entry."""
        self.size = self.size * 2
        new_table = [[] for _ in range(self.size)]

        for bucket in self.hash_table:
            for key, value in bucket:
                new_table[self._find_bucket(key)].append((key, value))

        self.hash_table = new_table