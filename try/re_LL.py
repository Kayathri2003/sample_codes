

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to reverse linked list
# using 3 pointer approach
def reverseLinkedList(head):
    
    # Initialize 'temp' at the
    # head of the linked list
    # temp = head
    
    # Initialize 'prev' to None,
    # representing the previous node 
    prev = None
    temp = head
    
    
    while temp is not None:
        # Store the next node in 'front'
        # to preserve the reference
        front = temp.next
        # Reverse the direction of the current
        # node's 'next' pointer to point to 'prev'
        temp.next = prev
        # Move 'prev' to the current 
        # node, for the next iteration
        prev = temp
        # Move 'temp' to 'front' node
        # advancing traversal
        temp = front

    # Return the new head
    # of the reversed linked list
    return prev
    
# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Create a linked list with
# values 1, 3, 2, and 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

# Print the original linked list
print("Original Linked List:", end=" ")
print_linked_list(head)

# Reverse the linked list
head = reverseLinkedList(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
print_linked_list(head)


