#2. Add Two Numbers

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        head1 = l1
        head2 = l2

        if type(head1) is None or type(head2) is None:
            return 0
        
        
        head3 = ListNode(head1.val + head2.val)
        if len(str(head3.val)) > 1:
            carry = str(head3.val)[0]
            head3.val = int(str(head3.val)[1])
        head1 = head1.next
        head2 = head2.next

        current = head3

        while head1 is not None or head2 is not None:

            if head1 is None:
                head1 = ListNode(0)
            if head2 is None:
                head2 = ListNode(0)

            print("head1: ", head1.val, "head2: ", head2.val, "carry: ", carry)

            current.next = ListNode(int(head1.val) + int(head2.val) + int(carry))
            carry = 0
            current = current.next
            if len(str(current.val)) > 1:
                carry = int(str(current.val)[0])
                current.val = int(str(current.val)[1])

            print("current: ", current.val, "new carry: ", carry)

            head1 = head1.next
            head2 = head2.next
        if carry != 0:
            current.next = ListNode(carry)

        display_linked_list(head3) # debug
        # print("done")
        return head3
                
       
def main():
    l1_values,l2_values = [9,9,9,9,9,9,9],[9,9,9,9]

    l1 = create_linked_list(l1_values)
    l2 = create_linked_list(l2_values)  

    # print("Linked List l1:")
    # display_linked_list(l1)

    # print("Linked List l2:")
    # display_linked_list(l2)

    solution = Solution()
    solution.addTwoNumbers(l1,l2)

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def display_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

main()