def deleteNode(head, position):
    if head.next == None:
        head = None

    elif position == 0:
        head = head.next

    else:
        temp = head
        count = 1

        while temp != None and count < position:
            temp = temp.next
            count += 1

        temp.next = temp.next.next

    return head
