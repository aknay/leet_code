from helpers.link_list import LinkListHelper, ListNode


# Title: 876. Middle of the Linked List
# Solution Ref: Official: Approach 2: Fast and Slow Pointer

##### start of solution

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next  # fast will travel twice as fast
        return slow  # will be in the middle


##### end of solution

#### test

#### case 1
llh = LinkListHelper()
llh.insert(1)
llh.insert(2)
llh.insert(3)
llh.insert(4)
llh.insert(5)
s = Solution()
result = s.middleNode(llh.head)
assert LinkListHelper.to_array(result) == [3, 4, 5]

#### case 2
llh = LinkListHelper()
llh.insert(1)
llh.insert(2)
llh.insert(3)
llh.insert(4)
llh.insert(5)
llh.insert(6)
s = Solution()
result = s.middleNode(llh.head)
assert LinkListHelper.to_array(result) == [4, 5, 6]
