class HashTable:
    def __init__(self):
        self.collection = {}
    
    def __str__(self):
        dic = f'{self.collection}'
        return dic
    
    def hash(self, key):
        hash_sum = 0
        for letter in key:
            hash_sum += ord(letter)
        return hash_sum
    
    def add(self, new_key, new_value):
        hash = self.hash(new_key)

        if not hash in self.collection:
            new = {hash : {new_key : new_value}}
            self.collection.update(new)
        
        else:
            old_values = self.collection[hash]
            new_values = {new_key : new_value}

            self.collection[hash] = old_values | new_values

    def remove(self, key):
        hash = self.hash(key)

        if hash in self.collection and key in self.collection[hash]:
            self.collection[hash].pop(key)
        else:
            return None
    
    def lookup(self, key):
        hash = self.hash(key)
        if hash in self.collection:
                if key in self.collection[hash]:
                    return self.collection[hash][key]
        else:
            None