
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: ?
    # Space Complexity: ?
    def get_first(self):
        if self.head:
            return self.head.value
        return None


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def add_first(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head)
        self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: ?
    # Space Complexity: ?
    def search(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: ?
    # Space Complexity: ?
    def get_at_index(self, index):
        cur_index = 0
        current = self.head
        while current:
            if cur_index == index:
                return current.value
            current = current.next_node
            cur_index += 1

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: ?
    # Space Complexity: ?
    def get_last(self):
        if self.head == None:
            return None
        current = self.head
        while current.next_node != None:
            current = current.next_node
        return current.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def add_last(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next_node != None:
                current = current.next_node
            current.next_node = Node(value)

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if self.head == None:
            return None
        cur_max = self.head.value
        current = self.head
        while current:
            if current.value > cur_max:
                cur_max = current.value
            current = current.next_node
        return cur_max

    # method to delete the first node found with specified value
    # Time Complexity: ?
    # Space Complexity: ?
    def delete(self, value):
        if self.head == None:
            return None
        elif self.head.value == value:
            self.head = self.head.next_node
        else:
            prev = self.head
            current = prev.next_node
            while current:
                if current.value == value and current.next_node:
                    prev.next_node = current.next_node
                    break
                elif current.value == value and current.next_node == None:
                    prev.next_node = None
                    break
                prev = current
                current = current.next_node



    # method to print all the values in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: ?
    # Space Complexity: ?
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            nxt_node = current.next_node
            current.next_node = prev
            prev = current
            current = nxt_node
        
        self.head = prev
        
        

    def get_last_node(self):
        if self.head == None:
            return None
        current = self.head
        while current.next_node != None:
            current = current.next_node
        return current

    def remove_last_node(self):
        if self.head == None:
            return None
        prev = self.head
        current = prev.next_node
        while current:
            if current.next_node == None:
                prev.next_node = None
            prev = current
            current = current.next_node

    ## Advanced/ Exercises
    def count_nodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def find_middle_value(self):
        count = self.count_nodes()
        return self.get_at_index(count // 2)

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        count = self.count_nodes()
        return self.get_at_index(count - n - 1)

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        seen = set()
        current = self.head
        while current:
            if current in seen:
                return True
            seen.add(current)
            current = current.next_node
        return False

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next_node != None:
            current = current.next_node

        current.next_node = self.head # make the last node link to first node
