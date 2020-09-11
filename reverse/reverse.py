class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is None:
            return None
        # if list has only 1 node
        if node.next_node is None:
            self.head = node
            return node

        temporary_node = self.reverse_list(node.get_next(), node)
        temporary_node.next_node = node
        node.set_next(None)

        return node


# RECURSIVE
#  1=>2=>3=>None

#  3=>2=>1=>None
 # 1st case: check if node passed in none, return none
 # 2nd case: is node.next is none, set the head to the node to make it first and return the node
 # 3rd case: create temporary node = recursive reverse method
 # After recursive call, reverse the order
 # set temp.node = node
 # node.next = None
 # return node
