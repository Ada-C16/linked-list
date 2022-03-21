
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.previous = prev_node

# Defines the singly linked list


class LinkedList:
    def __init__(self):
        self.head = None  # keep the head private. Not accessible outside this class
        self.tail = None

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
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            new_node = Node(value, self.head)
            self.head.previous = new_node
            self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        if self.head is None:
            return False

        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current.previous = current
                current = current.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        list_length = 0
        current = self.head

        while current is not None:
            list_length += 1
            current = current.next

        return list_length

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        current = self.head
        current_index = 0
        if index < 0 or current is None:
            return None

        while current_index <= index:
            if current_index != index:
                current = current.next
                current_index +=1
            elif current_index == index:
                return current.value

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def get_last(self):
        current = self.head
        if current is None:
            return None
        else:
            while current:
                if current.next is None:
                    return current.value
                else:
                    current = current.next

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def add_last(self, value):
        current = self.head
        # new_node = Node(value, next_node = current, prev_node = None)
        if self.head is None:
            self.head = Node(value)

        while current is not None:
            if current.next is None:
                new_node = Node(value, next_node=None, prev_node=current)
                self.tail = new_node
                current.next = new_node  # connect tail to new node
                current = current.next  # connect new node to tail
                return
            else:
                current = current.next

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        max_value = None
        current = self.head
        if current is None:
            return None
        else:
            while current:
                if (max_value is None) or (current.value > max_value):
                    max_value = current.value
                else:
                    current = current.next

        return max_value

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        current = self.head
        if current is None:
            return None

        if self.head.value == value:  # check for first
            self.head = self.head.next
            return

        while current:
            if current.next.value != value:
                current = current.next
            else:
                current.next = current.next.next
                return

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

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        if self.head is None:
            return None

        current = self.head
        previous = None

        while current is not None:
            next = current.next # track next node
            current.next = previous # change next node to previous node/switching
            previous = current # previous is pointing to something instead of None
            current = next # current shifts to the next node of the original, which is now previous

        self.head = previous # head now points to what is the former last item


    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n) My thinking is because, even though I index directly, I use the length method O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        list_length = self.length()

        search = list_length // 2
        
        return self.get_at_index(search)

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        desired_index = self.length() - n - 1
        
        return self.get_at_index(desired_index)

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def has_cycle(self):
        current = self.head
        has_visited = []
        
        if current is None:
            return False
        else:
            while current:
                has_visited.append(current)
                if current.next in has_visited:
                    return True
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

        current.next = self.head  # make the last node link to first node
