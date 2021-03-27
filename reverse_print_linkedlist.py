# HackerRank Challenge: Print in Reverse - Problem Solving -> Data Structures

def reversePrint(head):
    result = []
    current = head
    while (current):
        result.append(current.data)
        current = current.next

    for i in reversed(result):
        print(i)
