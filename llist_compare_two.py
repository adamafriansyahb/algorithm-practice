def compare_lists(llist1, llist2):
    while llist1 and llist2:
        if llist1.data == llist2.data:
            llist1 = llist1.next
            llist2 = llist2.next
        else:
            return 0

    return 1 if llist1 == None and llist2 == None else 0
