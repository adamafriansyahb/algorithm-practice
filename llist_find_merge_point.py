def findMergeNode(head1, head2):
    curr_1 = head1
    curr_2 = head2

    while (curr_1 != curr_2):
        curr_1 = curr_1.next if curr_1 != None else head2
        curr_2 = curr_2.next if curr_2 != None else head1

    return curr_1.data
