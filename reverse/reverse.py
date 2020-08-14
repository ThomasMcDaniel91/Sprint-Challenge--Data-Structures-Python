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
        #checking for empty list
        if self.head is None:
            return
        # checks to see if the head is the only node
        if self.head.next_node is None:
            return self.head
        else:
            # if the ll isn't only 1 node
            # assign a previous, current and next node variable
            prev = None
            current = self.head
            following = current.next_node
            # while we still have a current node, iterate through the list
            while current:
                # assign the nodes next value as it's previous
                current.next_node = prev
                # assign the previous node to the current
                prev = current
                # moving along the list
                current = following
                if following:
                    # assigns the next node variable to it's next value
                    following = following.next_node
        # once it's done looping in the while loop, assign the head to the last previous value
        self.head = prev
