
# # Defines a node in the singly linked list
# class Node:

#     def __init__(self, value, next_node = None, previous_node = None):
#         self.value = value
#         self.next = next_node
#         self.previous = previous_node

# # Defines the singly linked list
# class LinkedList:
#     def __init__(self):
#         self.head = None # keep the head private. Not accessible outside this class
#     # returns the value in the first node
#     # returns None if the list is empty
#     # Time Complexity: O(1)
#     # Space Complexity: 0(1)
#     def get_first(self):
#         if self.head == None:
#             return None
#         else:
#             return self.head.value


#     # method to add a new node with the specific data value in the linked list
#     # insert the new node at the beginning of the linked list
#     # Time Complexity: O(1)
#     # Space Complexity: O(1)
#     def add_first(self, value):
        # if not self.head:
        #     new_node = Node(value)
        #     self.head = new_node
        # new_node = Node(value)
        # new_node.next = self.head 
        # self.head= new_node  # Make the head point to the new node
        # return self.head  


#     # method to find if the linked list contains a node with specified value
#     # returns true if found, false otherwise
#     # Time Complexity: O(n)
#     # Space Complexity: O(1)
#     def search(self, value):
#         temp= self.head     
#         while temp:   
#             if temp.value == value:
#                 return True
#             temp = temp.next

#         return False
#     # method that returns the length of the singly linked list
#     # Time Complexity: ?
#     # Space Complexity: ?
#     def length(self):
#         current = self.head
#         length = 0

#         while current.next is not None:
#             length +=1
#             current = current.next
#         return length




#     # method that returns the value at a given index in the linked list
#     # index count starts at 0
#     # returns None if there are fewer nodes in the linked list than the index value
#     # Time Complexity: ?
#     # Space Complexity: ?
#     def get_at_index(self, index):
#         pass

#     # method that returns the value of the last node in the linked list
#     # returns None if the linked list is empty
#     # Time Complexity: O(n)
#     # Space Complexity: O(1)
#     def get_last(self):
        # if self.get_first() is None:
        #     return
        # temp = self.head 
        # while temp.next is not None:
        #     temp = temp.next

        # return temp.value

#     # method that inserts a given value as a new last node in the linked list
#     # Time Complexity: O(n)
#     # Space Complexity: O(1)
#     def add_last(self, value):
        # if self.get_first() is None:
        #     return
        # new_node = Node(value)
        # temp = self.head 

        # while temp.next:
        #     temp = temp.next

        # temp.next = new_node
        # print(temp.next.value)
        # return temp.next.value
    
#     # method to return the max value in the linked list
#     # returns the data value and not the node
#     def find_max(self):
#         pass

#     # method to delete the first node found with specified value
#     # Time Complexity: O(n)
#     # Space Complexity: 0(1)
#     def delete(self, value):

#         if self.head == None:
#             return None
#         if  value == self.head.value and self.head.next is None:
#             self.head = None
#             return
#         if  value == self.head.value:
#             self.head=self.head.next
#             return
#         current = self.head
#         while current.next is not None:
#             if value == current.next.value:
#                 break
#             current = current.next
#         if current.next is None:
#             print("Node not found") 
#         else:
#             current.next = current.next.next
    

#     # method to print all the values in the linked list
#     # Time Complexity: ?
#     # Space Complexity: ?
#     def visit(self):
#         helper_list = []
#         current = self.head

#         while current:
#             helper_list.append(str(current.value))
#             current = current.next
        
#         print(", ".join(helper_list))

#     # method to reverse the singly linked list
#     # note: the nodes should be moved and not just the values in the nodes
#     # Time Complexity: ?
#     # Space Complexity: ?
#     def reverse(self):
#         pass

#     ## Advanced/ Exercises
#     # returns the value at the middle element in the singly linked list
#     # Time Complexity: ?
#     # Space Complexity: ?
#     def find_middle_value(self):
#         pass

#     # find the nth node from the end and return its value
#     # assume indexing starts at 0 while counting to n
#     # Time Complexity: ?
#     # Space Complexity: ?
#     def find_nth_from_end(self, n):
#         pass

#     # checks if the linked list has a cycle. A cycle exists if any node in the
#     # linked list links to a node already visited.
#     # returns true if a cycle is found, false otherwise.
#     # Time Complexity: ?
#     # Space Complexity: ?
#     def has_cycle(self):
#         pass

#     # Helper method for tests
#     # Creates a cycle in the linked list for testing purposes
#     # Assumes the linked list has at least one node
#     def create_cycle(self):
#         if self.head == None:
#             return

#         # navigate to last node
#         current = self.head
#         while current.next != None:
#             current = current.next

#         current.next = self.head # make the last node link to first node


# llst = LinkedList()

# # print(llst.print_list())
# # print(llst.add_last(5))
# llst.add_first(5)
# llst.add_first(4)
# llst.add_first(3)

# print(llst.delete(2))
# print(llst.get_last())
# llst.delete(5)


# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class


    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: 0(1)
    def get_first(self):
        if self.head == None:
            return None
        else:
            return self.head.value

    # Add element at the head of the list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head 
        self.head= new_node  
        return self.head 
        
    # Search for a specific node 
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        temp= self.head     
        while temp:   
            if temp.value == value:
                return True
            temp = temp.next
        return False

    # Return the length of the ll 
    # Time Complexity: O(n)
    # Space Complexity: O(1)    
    def length(self):
        if self.head == None:
            return 0
        current = self.head
        length = 0
        while current is not None:
            length+= 1
            current = current.next
        return length

    
    # Find a node at a specific position - index
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        lst_length = self.length()
        # list is empty
        if self.head == None:
            return None
        # index passed is greater than tOTAL LEN 
        if lst_length < index:
            return None
        current = self.head
        idx = 0
        while current != None and idx < lst_length:
            if idx == index:
                return current.value
            # add +1 in idx - which is the current index
            idx += 1
            # point current to the next node
            current = current.next
        

    # Find the last node of a LL
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if self.get_first() is None:
            return
        temp = self.head 
        while temp.next is not None:
            temp = temp.next
        return temp.value

    
    # Asdd node at the end of the list - BIG-O
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        temp = self.head

        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        return

    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity:O(n)
    # Space Complexity: O(n)
    def find_max(self):
        # check if list is empty
        if self.head is None:
            return
        max_value = None
        current = self.head
        # check each node's value and compara if > max_value
        while current is not None:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        # return the value itself 
        return max_value


    # DELETION BIG-O
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        # check if list is empty
        if self.head == None:
            return None
        # if value == first node
        if  value == self.head.value:
            self.head=self.head.next
            return
        current = self.head

        while current.next is not None:
            # stop when find the value 
            if value == current.next.value:
                break
            current = current.next

        # if value not found
        if current.next is None:
            return None
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


    # method to reverse ll
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
    # check if list is empty
        if self.head == None:
            return None

        previous = None
        current = self.head

        # loop until we reach the last node

        # null  <-| 1 |<-| 2 |<-| 3 |

        while current is not None:
            # save next_node 
            temp = current.next
            current.next = previous
            previous = current 
            current = temp
        
        self.head= previous


    # OPTIONAL FUNCTIONS - I will be implementing these in the future
    # Advanced/ Exercises
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