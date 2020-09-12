class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if the root node's value equals the target
        if target == self.value:
            return True
        # check if the root's value is less than the target
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # check if the root's value is greater than the target
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
