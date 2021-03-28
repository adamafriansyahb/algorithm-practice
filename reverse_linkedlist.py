# HackerRank Challange: Reverse a Linked List - Problem Solving -> Data Structures

def reverse_llist(head):
    current = head
    prev = None
    after = current.next

    while current:
        after = current.next
        current.next = None
        prev = current
        current = after

    # Prev is returned as head
    return prev
