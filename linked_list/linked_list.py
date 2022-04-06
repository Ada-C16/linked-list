
# Defines a node in the singly linked list
from re import L


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
        return self.head.value if self.head else None


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return self.head.value


    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def search(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return True
            cur = cur.next
        else:
            return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def length(self):
        length = 0
        cur = self.head
        while cur is not None:
            length += 1
            cur = cur.next
        return length         

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        cur = self.head
        while cur is not None and index != 0:
            index -= 1
            cur = cur.next
        if index == 0:
            return cur.value
        else:
            return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def get_last(self):
        if self.head is None:
            return None
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        return cur.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def add_last(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node
        return self.head


    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if self.head is None:
            return None
        max_val = self.head.value
        cur = self.head
        while cur is not None:
            if cur.value > max_val:
                max_val = cur.value
            cur = cur.next
        return max_val

    # method to delete the first node found with specified value
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def delete(self, value):
        if self.head is None:
            return None
        cur = self.head
        dummy = Node(0)
        dummy.next = self.head
        pre = dummy
        while cur is not None:
            if cur.value == value:
                cur = cur.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next
        self.head = dummy.next
        return self.head.value

    # method to print all the values in the linked list
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def reverse(self):
        if self.head is None or self.head.next is None:
            return self.head
        pre = Node(0)
        cur = self.head
        nxt = self.head
        while cur is not None:
            nxt = nxt.next
            cur.next = pre
            pre = cur
            cur = nxt
        self.head = pre
        return pre
        
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def find_middle_value(self):
        if self.head is None or self.head.next is None:
            return self.head        
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow.value

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):      
        fast = self.head
        slow = self.head      
        while fast is not None and n != 0:
            fast = fast.next 
            n -= 1
        if fast is None:
            return None
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        return slow.value


    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def has_cycle(self):
        if self.head is None or self.head.next is None:
            return False
        fast = self.head
        slow = self.head  
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        else:
            return False                

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
