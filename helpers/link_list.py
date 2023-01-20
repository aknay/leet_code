from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkListHelper(object):
    def __init__(self):
        self.head = None

    def insert(self, v):
        newNode = ListNode(v)
        if self.head is None:
            self.head = newNode
            return

        head = self.head
        while head.next is not None:
            head = head.next
        head.next = newNode

    def print(self):
        head = self.head
        while head is not None:
            print(head.val)
            head = head.next

    @staticmethod
    def to_array(v: ListNode) -> List[int]:
        ar = []
        while v is not None:
            ar.append(v.val)
            v = v.next
        return ar
