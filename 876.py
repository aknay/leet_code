from helpers.link_list import LinkListHelper, ListNode

llh = LinkListHelper()
llh.insert(1)
llh.insert(2)
llh.insert(3)
llh.insert(4)
llh.insert(5)


##### start of solution

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


s = Solution()
result = s.middleNode(llh.head)
assert LinkListHelper.to_array(result) == [3, 4, 5]
