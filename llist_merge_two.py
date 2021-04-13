def mergeLists(head1, head2):
    temp = SinglyLinkedListNode(0)
    current = temp

    while head1 and head2:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next

        current = current.next

    if head1:
        current.next = head1
        head1 = head1.next

    if head2:
        current.next = head2
        head2 = head2.next

    return temp.next
