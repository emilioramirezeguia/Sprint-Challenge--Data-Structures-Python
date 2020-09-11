class RingBuffer:
    def __init__(self, capacity):
        self.top_item = None
        self.capacity = capacity
        self.storage = [] * capacity
        self.tail = -1
        self.head = 0
        self.size = 0

    def append(self, item):
        if self.is_full():
            return None  # Buffer is full
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.storage[self.tail] = item
            self.size = self.size + 1

    def get(self):
        if self.is_empty():
            return None  # Buffer is empty
        else:
            tmp = self.storage[self.head]
            self.head = (self.head + 1) % self.capacity

        self.size = self.size - 1
        return tmp

    def display(self):
        if self.is_empty():
            print("Buffer is empty.")
        else:
            index = self.head

            for i in range(self.size):
                print(self.storage[index])
                index = (index + 1) % self.capacity

    # def peek(self):
    #     if self.is_empty() is not None:
    #         return self.top_item.get_value()
    #     else:
    #         print("Buffer is empty.")

    def is_full(self):
        return self.capacity == len(self.storage)

    def is_empty(self):
        return self.capacity == 0
