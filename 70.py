# Title: 70. Climbing Stairs


class Solution:
    def fib(self, n: int) -> int:
        return self._climb_bottom_up(n)
        # return self._fib_r(n)

    def _climb_r(self, num):
        # climbing recursively
        if num <= 3:
            return num
        return self._climb_r(num - 1) + self._climb_r(num - 2)

    def _climb_bottom_up(self, n) -> int:
        # fib is  -> 0 1 1 2 3 5 8
        # this is -> 0 1 2 3 5 8
        ar = [0, 1, 2, 3]
        for i in range(4, n + 1):  # it starts to change from index 4, from 0 to 3 indexes are same as result 0 to 3
            ar.append(ar[i - 1] + ar[i - 2])  # add from previous two indexes
        return ar[n]


#### test

#### case 1
s = Solution()
result = s.fib(2)
assert result == 2

#### case 2
s = Solution()
result = s.fib(3)
assert result == 3

#### case 3
s = Solution()
result = s.fib(5)
assert result == 8
