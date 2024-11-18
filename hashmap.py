# Noah Preston , CSC-231 - 001

class Node:
    def __init__(self, key, value):
        self.key = key  # Store key for the node
        self.value = value  # Store value 
        self.next = None  # Set next node to None

class HashMap:
    def __init__(self, size = 150):
        self.size = size  # Set size of the hash table
        self.table = [None] * size  # Create an empty table 
        self.keys = []  # List to store keys

    def _hash(self, key): # Using Python function and modulo for index
        return hash(key) % self.size  

    def __setitem__(self, key, value):
        index = self._hash(key)  # Index for the key
        if self.table[index] is None: # If table is empty for index then insert new node
            self.table[index] = Node(key, value)
            self.keys.append(key)  # Add key to the keys list
        else: # Traversing linked list and preventing collisions 
            current = self.table[index]
            while current:
                if current.key == key: 
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, value) # Add a new node 
            self.keys.append(key) # Append key 

    def __getitem__(self, key):
        index = self._hash(key)  # Index for the key
        current = self.table[index]  # Start at first node
        while current:
            if current.key == key:
                return current.value
            current = current.next  # Move to next node in list 
        raise KeyError(f"Key {key} not found.")  # Raise error if key is not found

    def __delitem__(self, key):
        index = self._hash(key)  # Index for the key
        current = self.table[index]  # Start at the first node 
        prev = None # Set previous node for linking
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.keys.remove(key)  # Remove key from list
                return
            prev = current  # Previous node to current node
            current = current.next  # Move to next node
        raise KeyError(f"Key {key} not found.")  # Raise error if key is not found

    def __contains__(self, key):
        index = self._hash(key)  # Index for the key
        current = self.table[index]  # Start at first node 
        while current:  # Traverse linked list to search
            if current.key == key:  
                return True # Returns True if the key matches
            current = current.next  # Move to the next node in the linked list
        return False  # Returns False if key is not found

    def get_keys(self):
        return self.keys  # Returns the list of keys
