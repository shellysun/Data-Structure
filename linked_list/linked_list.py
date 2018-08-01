"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""


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
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value) # consitant
        # check if the head of linkedlist is empty
        # if the head node is empty, the new node can just add as a tail node
        if self.head is None:
            self.head = new_node
            # get the tail
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            # update the tail
            self.tail = new_node

    def remove_head(self):
        # check if the head node is empty
        if self.head is None:
            return None
        # if we have single element list, we remove it and left empty list
        if self.head is not None:
            head = self.head
            # delete
            self.head = None
            # make sure the tail points to None
            self.tail = None
            return head.value

        else:
            # we have multiple
            value = self.head.value
            self.head = self.head.next
        return value

    def contains(self):
        # check to see if the list is empty
        if self.head is None:
            return None
        # assign the current node to a variable
        current = self.head
        # iterate through the list
        while current:
            if current.value == value:
                return True
            # move on to the next list node
            # by updating 'current'
            current = current.get_next()
        return False

    def get_max(self):
        # if there is empty
        if self.head == None:
            return None

        # set current to head's 'next'
        current = self.head.get_next()
        max_value = self.head.value

        while current:
            if max_value < current.value:
                max_value = current.value
            current = current.next_node
        return max_value
