class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current_index = 0

    def append(self, item):
        # append at the head index
        self.storage[self.current_index] = item
        # then increment the current_index
        self.current_index += 1
        # don't go over capacity, so check if current_index is equal to capacity
        if self.current_index == self.capacity:
            self.current_index = 0
        # if it is, reset current_index to 0

    def get(self):
        filtered_data = [
            element for element in self.storage if element is not None]
        return filtered_data
