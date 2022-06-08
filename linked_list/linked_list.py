

class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self):
      self.head = None 
    def get_first(self):
        if self.head:
            return self.head.value
        return None

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        self.head = Node(value, self.head)

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def search(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next

        return count

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def get_at_index(self, index):
        current_index = 0
        current = self.head
        while current_index < index and current:
            current_index += 1
            current = current.next

        if current_index == index and current:
            return current.value
        return None

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def get_last(self):
        if not self.head:
            return None

        current = self.head
        while current.next:
            current = current.next

        return current.value

    # Time Complexity: O(n); more than 1 approach; same complexity 
    # Space Complexity: O(n); more than 1 approach; same complexity 
    def add_last(self, value):
        if not self.head:
            self.add_first(value)
        else:
            new_node = Node(value)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def find_max(self):
        if self.head == None:
            return None

        current = self.head
        max = self.head.value
        while current:
            if current.value > max:
                max = current.value
            current = current.next

        return max

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def delete(self, value):
        if not self.head:
            return

        if value == 0:
            self.head = self.head.next

        current = self.head
        current_index = 0
        while current.next and current_index < value - 1:
            current = current.next
            current_index += 1

        if current.next:
            current.next = current.next.next

    # Time Complexity: O(1) after element is found; O(n) prior
    # Space Complexity: O(1)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def reverse(self):
        if not self.head:
            return

        current = self.head
        previous = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def find_middle_value(self):
        if not self.head:
            return None

        return self.get_at_index(int(self.length() / 2))

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def find_nth_from_end(self, n):
        if not self.head:
            return None

        current = self.head
        trail = None
        spacing = 0
        while current and spacing < n:
            current = current.next
            spacing += 1

        if not current:
            return None

        trail = self.head
        while current.next:
            current = current.next
            trail = trail.next

        return trail.value

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
