""" You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero,
    except the number 0 itself. """


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):

    result = ListNode((l1.val + l2.val) % 10)

    carry = (l1.val + l2.val) // 10

    pointer = result

    first = l1.next
    second = l2.next

    while first or second or carry:

        pointer.next = ListNode(carry)
        pointer = pointer.next

        if first:
            pointer.val += first.val
            first = first.next

        if second:
            pointer.val += second.val
            second = second.next

        carry = pointer.val // 10
        pointer.val %= 10

    return result




