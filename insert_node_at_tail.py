# HackerRank challenge: Insert a Node at the Tail of a Linked List

def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if (head == None):
        head = node
    else:
        current = head
        while (current.next):
            current = current.next
        current.next = node

    return head
