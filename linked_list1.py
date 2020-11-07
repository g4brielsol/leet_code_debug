# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:  
        tail = head
        list_length = 1
        print(tail)
        if head is not None:
            # get tail and list size
            while tail.next is not None:
                tail = tail.next
                list_length += 1
            # make a circular linked list
            tail.next = head
            #when k is bigger than length, it is the same as doing k = k % length
            k = k % list_length
            # get how many steps to run through the linked list
            steps = list_length - k
            # got through the linked list
            for i in range(0, steps):
                before_node = head
                # new head at the end of for loop
                head = head.next
            # break circular linked list
            before_node.next = None
            return head
        
#       2->3->4->5->6->2, 1
#                b  h
        
        
#    2->3->4->5->6, 2
#    62345, 1, 5
#    56234, 2, 5
#    45623, 3, 5
#    34562, 4, 5
#    23456, 5, 5
#    62345, 6, 5 -> 1
    
    
    
#    3->4->5, 2
#    534, 1, 3
#    453, 2, 3
#    345, 3, 3
#    534, 4, 3 -> 1
#    453, 5, 3 -> 2
#    345, 6, 3 -> 0
    
#    3->4->5-
    
#    1->2, 4
#    21
#    12
#    21
#    12