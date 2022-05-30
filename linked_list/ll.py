# class Node:
#     def __init__(self, value, next=None):
#         self.data = value
#         self.data = next
# # it references the

# # add a node to the front of the list
# def add_first(current_head, new_value):
#     new_node= Node(new_value)
#     new_node.next = head
#     return new_node

# # make a function to get the last element of a linked list
# def get_last(head):
#     # edge case
#     if head == None:
#         return None

#     current = head
#     while current.next != None:
#         current = current.next

#     return current.data

# head = Node("Pizza")
# other_node = Node("Pasta")

# head.next = other_node

# ther_node = Node('Dumplings')

# head.next.next = other_node

# # how to print
# current = head

# while current != None:
#     print(current.data)
#     current = current.next

# # add a node to the front of the list
# new_node = Node('Tacos')
# new_node.next = head
# head = new_node

# head = add_first(head, 'Burrito')

# print('---------')
# while current != None:
#     print(current.data)
#     current = current.next

# # ******************************************************
# # encapsulation 
# class Node:
#     def __init__(self, value, next=None):
#         self.data = value
#         self.data = next


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def add_first(self, value):
#         # new_node = Node(value)

#         # new_node.next = self.head
#         # self.head = new_node
#         # orrrr
#         self.head = Node(value, self.head) 

#     def get_first(self):
#         if self.head == None:
#             return None
        
#         return self.head.data
    
#     def add_last(self, value):
#         pass

#     def get_last(self):
#         if self.head == None:
#             return None

#         current = self.head 

#         while current.next != None:
#             current = current.next

#         return current.data 
    
#     def find(self, value):
#         current = self.head

#         while current != None:
#             if current.data == value:
#                 return True
#             current = current.next
#         return False

# ****************************************************** below is my notes 
class Node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next

def add_first(current_head, new_value):
    new_node = Node(new_value)
    new_node.next = current_head
    return new_node

def get_last(head):
    if head == None:    
        return None
    current = head
    while current.next != None:
        current = current.next

    return current.data

head = Node('pizza')
other_node = Node('pasta')

head.next = other_node

other_node = Node('Dumplings')


head.next.next = other_node
#the code above links the nodes together


current = head
# the code below and above are how you print 
while current != None:
    print(current.data)
    current = current.next

# how do you add a node to the front of the list
new_node = Node('Tacos')
new_node.next = head
head = new_node