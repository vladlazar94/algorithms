# You are given two non-empty linked lists representing 
# two non-negative integers. 
# The digits are stored in reverse order and each of their 
# nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):

    result = ListNode(0)

    pointer = result 

    carry = 0

    l1temp = l1
    l2temp = l2

    while l1temp is not None or l2temp is not None:

        value = 0

        if l1temp is not None:
            value = value + l1temp.val

        if l2temp is not None:
            value = value + l2temp.val

        l1temp = l1temp.next
        l2temp = l2temp.next

        value = value + carry
        carry = value // 10
        value = value % 10

        pointer.val = value
        pointer.next = ListNode(0)
        pointer = pointer.next

    return result


test1 = ListNode(2)
test1.next = ListNode(4)
test1.next.next = ListNode(3)

test2 = ListNode(5)
test2.next = ListNode(6)
test2.next.next = ListNode(4)

temp_result = add_two_numbers(l1 = test1, l2 = test2)

x = 1