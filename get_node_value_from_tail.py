def getNode(head, positionFromTail):
    pointer = head
    count = 0

    while head.next:
        head = head.next

        if count < positionFromTail:
            count += 1
        else:
            pointer = pointer.next

    return pointer.data
