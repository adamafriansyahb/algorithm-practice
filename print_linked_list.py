# Print the Element of a Linked List - HackerRank

#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

# Complete the printLinkedList function below.

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next


def printLinkedList(head):
    current = head
    while (current):
        print(current.data)
        current = current.next


if __name__ == '__main__':

    llist = SinglyLinkedList()

    llist_item = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]

    for i in range(len(llist_item)):
        llist.insert_node(llist_item[i])

    printLinkedList(llist.head)
