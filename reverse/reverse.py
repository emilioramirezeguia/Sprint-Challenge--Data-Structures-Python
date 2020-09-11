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
        self.prev = None
        self.node = None
        # # exit out of the function if list is empty
        # if not self.head:
        #     return False

        # grab a hold of the starting node
        current = self.head

        # while a node exists
        while current:
            next = current.next_node
            current.next = prev
            prev = current
            current = next
        self.head = prev

        # # if the node has a next node
        # if current.next_node:
        #     # update the current node to be that node (go to that node)
        #     current = current.get_next()
        # else:
        #     current.next_node = self.head
        #     self.head = self.head.next_node

# RECURSIVE
 1=>2=>3=>None

 3=>2=>1=>None
 # 1st case: check if node passed in none, return none
 # 2nd case: is node.next is none, set the head to the node to make it first and return the node
 # 3rd case: create temporary node = recursive reverse method
 # After recursive call, reverse the order
 # set temp.node = node
 # node.next = None
 # return node