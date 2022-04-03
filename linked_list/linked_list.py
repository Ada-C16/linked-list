
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
      self.head = None # keep the head private. Not accessible outside this class

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head == None:
            return None
        value = self.head.value
        return value

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        if self.head == None:
            return False
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
            
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        if self.head == None:
            return 0
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        if self.head == None or self.length() < index:
            return None
        current = self.head
        current_index = 0
        while current is not None and current_index < self.length():
            if current_index == index:
                return current.value
            current_index += 1
            current = current.next

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if self.head == None:
            return None
        current = self.head
        while current.next is not None:
            current = current.next
        return current.value

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None :
            current = current.next
        current.next = new_node

    # Time Complexity:O(n)
    # Space Complexity: O(1)
    def find_max(self):
        if self.head is None:
            return
        max_value = None
        current = self.head
        while current is not None:
            if max_value is None or current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        if self.head == None:
            return None
        if  value == self.head.value and self.head.next is None:
            self.head = None
            return
        if  value == self.head.value:
            self.head=self.head.next
            return
        current = self.head
        while current.next is not None:
            if value == current.next.value:
                break
            current = current.next
        if current.next is None:
            print("Node not found") 
        else:
            current.next = current.next.next
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        if self.head == None:
            return
        if self.head.next is None:
            return self.head
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
  
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        if self.head == None:
            return
        if self.head.next is None:
            return self.head
        current = self.head
        count = 0
        n = self.length()//2
        while current is not None:
            if count == n:
                return current.value
            count += 1
            current = current.next

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        if self.head is None or (n+1) > self.length():
            return None 
        current = self.head
        count = 0
        len = self.length()
        while current is not None:
            if count == len - (n + 1):
                return current.value
            current = current.next
            count += 1

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def has_cycle(self):
        linked_set = set()
        current = self.head
        while current is not None:
            if current in linked_set:
                return True
            linked_set.add(current)
            current = current.next
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
