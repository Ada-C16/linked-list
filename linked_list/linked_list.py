class Node:
    '''
    Defines a node in the singly linked list
    '''

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    '''
    Defines the singly linked list
    '''

    def __init__(self):
        self.head = None  # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head is not None:
            return self.head.value
        else:
            return None

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def add_first(self, value):
        self.head = Node(value, next_node=self.head)

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        current_node = self.head
        length = 0
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        current_node = self.head
        current_index = 0
        while current_node is not None:
            if index == current_index:
                return current_node.value
            current_node = current_node.next
            current_index += 1
        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        current_node = self.head
        while current_node is not None:
            if current_node.next is None:
                return current_node.value
            current_node = current_node.next
        return None

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        last_node = self.head
        while last_node is not None:
            if last_node.next is None:
                break
            last_node = last_node.next

        if last_node is not None:
            last_node.next = Node(value)
        else:
            self.head = Node(value)

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        current_node = self.head
        if current_node is None:
            return None
        max_val = current_node.value
        while current_node is not None:
            max_val = max(current_node.value, max_val)
            current_node = current_node.next
        return max_val

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        # Head has the value to delete
        if self.head is not None\
                and self.head.value == value:
            self.head = self.head.next
            return

        current_node = self.head
        # value to delete is in not head
        while current_node is not None:
            next_node = current_node.next
            if next_node is not None\
                    and next_node.value == value:
                current_node.next = next_node.next
                return
            current_node = next_node

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
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def reverse(self):
        node_list = []
        current_node = self.head
        while current_node is not None:
            node_list.append(current_node)
            current_node = current_node.next

        for index in range(len(node_list)-1, 0, -1):
            try:
                node_list[index].next = node_list[index-1]
            except IndexError:
                node_list[index].next = None

        try:
            self.head = node_list[-1]
        except IndexError:
            self.head = None

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
