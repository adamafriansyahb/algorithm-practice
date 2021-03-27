# HackerRank Challenge: Insert a Node at the Head of The Linked List - Problem Solving -> Data Structures

def insertNodeAtHead(llist, data):
    node = SinglyLinkedListNode(data)

    if (llist == None):
        llist = node
    else:
        node.next = llist
        llist = node

    return llist
