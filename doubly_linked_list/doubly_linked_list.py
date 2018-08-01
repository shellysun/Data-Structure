class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        pass

    def insert_before(self, value):
        pass

    def delete(self):
        pass

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # no elements in the list
        if self.head is None:
            new_node = ListNode(value)
            new_node.prev = None
            self.head = new_node

        else:
            new_node = ListNode(value)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def remove_from_head(self):
        pass

    def add_to_tail(self, value):
      # if the head node is null -> empty list
        if self.head is None:
          # create a new node
             new_node = ListNode(value)
          # make sure the previous node point to none
             new_node.prev = None
          # update status of the head pointer
             self.head = new_node
          # at least on element in the list
        else:
          # create a new node
            new_node = ListNode(value)
          # check which element points to none
          # use while loop and find the last one
            current = self.head
            while current.next: # while current.next is not none
                current = current.next # update the current node
            new_node.prev = current
            new_node.next = None

    def remove_from_tail(self):
        pass

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):
        pass
