# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


# composition relationship to class Node
# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None  # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: constant, no traversing needed
    # Space Complexity: constant, no new data structures
    def get_first(self):
        if self.head is None:
            return None
        return self.head.value

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: constant
    # Space Complexity: constant
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head  # assign current head of linked list to the
        self.head = new_node  # assign new node to head

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: linear
    # Space Complexity: constant
    def search(self, value):
        if self.head is None:
            return False
        current_node = self.head
        target_node = Node(value)

        # traverse list til reach target node or end of list
        while current_node:
            if current_node.value == target_node.value:
                return True
            current_node = current_node.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def length(self):
        if self.head is None:
            return 0
        current_node = self.head
        length_of_list = 0

        # traverse list til reach end, increment length while traversing.
        while current_node:
            length_of_list += 1
            current_node = current_node.next

        return length_of_list

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: linear
    # Space Complexity: constant
    def get_at_index(self, index):
        if index < 0 or self.length() < index:
            return None
        current_index = 0
        current_node = self.head

        # traverse list till reach index or end of list
        while current_node:
            # can add a condition to check the current node is less than index if above does not work
            if current_index == index:
                break
            current_node = current_node.next
            current_index += 1

        return current_node.value

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: linear
    # Space Complexity: constant
    def get_last(self):
        if self.head is None:
            return None
        current_node = self.head
        tail_node = current_node
        prev_node = None

        # traverse list till reach end.
        while current_node:
            prev_node = current_node
            current_node = current_node.next
        tail_node = prev_node
        return tail_node.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: linear
    # Space Complexity: constant
    def add_last(self, value):
        if self.head is None:
            self.head = value
            return

        prev_node = None
        current_node = self.head
        new_tail_node = Node(value)

        # traverse list till reach end.
        while current_node:
            prev_node = current_node
            current_node = current_node.next
        # re-assign nodes so last node we found becomes second to last pointing to new tail and new tail points to none
        new_tail_node = prev_node
        current_node.next = new_tail_node
        new_tail_node.next = None

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if self.head is None:
            return None
        current_node = self.head
        max_node = current_node

        while current_node:
            if current_node.value > max_node.value:
                max_node = current_node
                current_node = current_node.next

        return max_node.value

    # method to delete the first node found with specified value
    # Time Complexity: linear
    # Space Complexity: constant
    def delete(self, value):
        if self.head is None:
            return
        current_node = self.head
        next_node = current_node.next
        target_value = value
        if current_node.value == target_value:
            current_node = current_node.next
            return
        while current_node:
            if next_node.value == target_value:
                current_node.next = next_node.next
                return
            current_node = current_node.next
            next_node = next_node.next
        return

    # method to print all the values in the linked list
    # Time Complexity: linear
    # Space Complexity: linear
    def visit(self):
        node_values = []
        current_node = self.head

        # traverse list,append values along the way.
        while current_node:
            node_values.append(str(current_node.value))
            current_node = current_node.next
        print(",".join(node_values))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: linear
    # Space Complexity: constant
    def reverse(self):
        if self.head is None:
            return
        current_node = self.head
        next_node = None
        prev_node = None

        # traverse list, reversing pointers along the way
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

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

        current.next = self.head  # make the last node link to first node
