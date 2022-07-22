
# Defines a node in the singly linked list
from threading import currentThread


class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head is None:
            return None

        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        self.head = Node(value, self.head)


    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False 
        
    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        current = self.head
        lenght_of_list = 0
        while current != None:
            lenght_of_list += 1
            current = current.next
        return lenght_of_list

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity:  O(n)
    # Space Complexity: 0(1)
    def get_at_index(self, index):
        current_node = self.head
        current_index = 0
        while current_node != None: 
            if current_index == index:
                return current_node.value
            current_index += 1
            current_node = current_node.next
        return current_node

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: 0(1)
    # Space Complexity: 0(1)
    def get_last(self):
        if self.length() is 0:
            return None
        return self.tail.value 

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: 0(1)
    # Space Complexity: 0(1)
    def add_last(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node


    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if self.head is None:
            return None 
        
        current = self.head
        max_value = current.value
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value

    # method to delete the first node found with specified value
    # Time Complexity: 0(n)
    # Space Complexity: 0(1)
    def delete(self, value):
        if self.head is None:
            return 
        if value == 0:
            self.head = self.head.next
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == value:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        return prev

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))
