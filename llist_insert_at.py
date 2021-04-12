def insertNodeAtPosition(head, data, position):
    newNode = SinglyLinkedListNode(data)

    if (head):
        temp = head
        count = 1
        while temp != None and count < position:
            temp = temp.next
            count += 1

        newNode.next = temp.next
        temp.next = newNode

    else:
        head = newNode

    return head
