class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        print(l1.val)
        l1_arr = []
        l2_arr = []
        while l1:
            l1_arr.append(str(l1.val))
            l1 = l1.next
        while l2:
            l2_arr.append(str(l2.val))
            l2 = l2.next
        l1_arr = int("".join(l1_arr[::-1]))
        l2_arr = int("".join(l2_arr[::-1]))
        res = str(l1_arr + l2_arr)[::-1]
        
        _res = [int(num) for num in res]
        
        
        l = ListNode(0)
        next_node = l
        for num in _res:
            next_node.next = ListNode(num)
            next_node = next_node.next
        return l.next