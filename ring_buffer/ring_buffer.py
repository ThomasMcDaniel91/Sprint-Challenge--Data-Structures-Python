class RingBuffer:
    def __init__(self, capacity):
        # assigning the max capacity
        self.capacity = capacity
        # giving the class a way to store values
        self.storage = []
        # attribute to keep track of the index to remove
        self.current = 0

    def append(self, item):
        # if we are still inside capacity just append the item to the storage
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            # add 1 to the current attribute
            self.current += 1
        else:
            # if the storage is full, we overwrite the value at the current index
            self.storage[self.current] = item
            # add 1 to the current
            self.current += 1
        # at the end of appending the item, check to see if the current index
        # needs to be reset to start back at the beginning
        if self.current >= self.capacity:
            # if it is at the end of the capacity then reset it to 0
            self.current = 0

    def get(self):
        return self.storage