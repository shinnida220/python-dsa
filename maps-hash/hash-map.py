# Hash Map
class HashMap(object):
    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size

    # Helper function that computes hash
    def _get_hash(self, key):
        hash = 0
        # loop through each character and convert to ascii
        for char in key:
            hash *= ord(char)  # causes a lot of collison
            # hash += ord(char) # reduces collision
        return hash % self.size

    def store(self, key, value):
        key_index = self._get_hash(key)
        key_value = [key, value]

        # check if the index has an element alread
        if self.table[key_index] is None:
            self.table[key_index] = list([key_value])
            return True
        else:
            # lets go thru the elements at this index
            # to see if this key exist
            # if it does, we update. if not we append
            for pair in self.table[key_index]:
                if pair[0] == key:
                    pair[1] = value
                    return True

            # At this point we know its not there, we need to add it
            self.table[key_index].append(key_value)
            return True

    def get(self, key):
        key_index = self._get_hash(key)

        if self.table[key_index] is not None:
            for pair in self.table[key_index]:
                if pair[0] == key:
                    return pair[1]

        # Key not found
        return None

    def delete(self, key):
        key_index = self._get_hash(key)

        if self.table[key_index] is not None:
            for i in range(0, len(self.table[key_index])):
                if self.table[key_index][i][0] == key:
                    self.table[key_index].pop(i)
                    return True
        # Key not found
        return False

    def print(self):
        print('--- Printing HashTable ---')
        for item in self.table:
            if item is not None and len(item) > 0:
                print(str(item))
        print('--- End Printing HashTable ---')


h = HashMap()
h.store('Bob', '567-8888')
h.store('Ming', '293-8888')
h.store('Ming', '333-8233')
h.store('Ankit', '293-8625')
h.store('Aditya', '852-6551')
h.store('Alicia', '632-4123')
h.store('Mike', '567-2188')
h.store('Aditya', '777-8888')
h.print()
h.delete('Bob')
h.print()
print('Ming: ' + h.get('Ming'))
