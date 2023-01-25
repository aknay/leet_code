# Title: 509. Fibonacci Number

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.


class Solution:
    def fib(self, n: int) -> int:
        return self._fib_bottom_up(n)

    def _fib_r(self, num):
        if num <= 1:
            return num
        return self._fib_r(num - 1) + self._fib_r(num - 2)

    def _fib_bottom_up(self, n) -> int:
        # ref: https://www.mathsisfun.com/numbers/fibonacci-sequence.html
        # ref: https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/m2G1pAq0OO0
        #  xn = xn−1 + xn−2
        # 0 1 1 2 3 5 8 13
        #         | |
        #             |
        # adding previous 3 and 5 will get next value 8
        ar = [0, 1]
        for i in range(2, n + 1):
            ar.append(ar[i - 1] + ar[i - 2])
        return ar[n]


#### test

#### case 1
s = Solution()
result = s.fib(2)
assert result == 1

#### case 2
s = Solution()
result = s.fib(3)
assert result == 2

#### case 3
s = Solution()
result = s.fib(4)
assert result == 3
