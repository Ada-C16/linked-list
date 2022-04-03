
# Defines a node in the singly linked list
from unittest.mock import sentinel


class Node:

    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.__sentinel = Node(None)
        self.__sentinel.next = self.__sentinel
        self.__sentinel.prev = self.__sentinel
        self.__length = 0

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        return self.__sentinel.next.value

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value, self.__sentinel.next, self.__sentinel)
        self.__sentinel.next = new_node
        new_node.next.prev = new_node
        self.__length += 1

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current_node = self.__sentinel.next

        while(current_node.value is not None):
            if current_node.value == value:
                return True
            current_node = current_node.next

        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def length(self):
        return self.__length

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        current_node = self.__sentinel.next
        while(index > 0):
            if current_node.value is None: return None
            current_node = current_node.next
            index -= 1
        return current_node.value

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_last(self):
        return self.__sentinel.prev.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_last(self, value):
        new_node = Node(value, self.__sentinel, self.__sentinel.prev)
        self.__sentinel.prev = new_node
        new_node.prev.next = new_node
        self.__length += 1

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        current_node = self.__sentinel.next
        max_value = None

        while current_node.value is not None:
            max_value = max(max_value, current_node.value) if max_value else current_node.value
            current_node = current_node.next

        return max_value

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        current_node = self.__sentinel.next

        while current_node.value is not None:
            if current_node.value == value:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                self.__length -= 1
                return

            current_node = current_node.next

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def visit(self):
        helper_list = []
        current = self.sentinel.next

        while current.value:
            helper_list.append(str(current.value))
            current = current.next

        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: I think O(1) because delete method is always on first node
    # Space Complexity: O(n)
    def reverse(self):
        list_len = self.length()
        new_list = LinkedList()

        for i in range(list_len):
            first_value = self.get_first()
            self.delete(first_value)
            new_list.add_first(first_value)

        self.__sentinel.next = new_list.__sentinel.next
        self.__sentinel.prev = new_list.__sentinel.prev

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def find_middle_value(self):
        pass

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        pass

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        pass

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
