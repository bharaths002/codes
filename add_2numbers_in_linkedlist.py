class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self,l1:ListNode ,l2:ListNode)->ListNode:
        dummy=ListNode()
        cur=dummy
        carry=0

        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
 
        #new digit 
            val= v1+v2+carry
            carry=val // 10
            val=val % 10

            cur.next=ListNode(val)

            #update ptrs
            cur=cur.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return dummy.next    


# Helper function to create a linked list from a Python list
def create_linked_list(numbers):
    dummy = ListNode()
    cur = dummy

    for num in numbers:
        cur.next = ListNode(num)
        cur = cur.next

    return dummy.next


# Helper function to print the linked list
def print_linked_list(head):
    while head:
        print(head.val, end="")
        if head.next:
            print(" -> ", end="")
        head = head.next
    print()


# Input: 342 + 465 = 807
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

print_linked_list(result)
