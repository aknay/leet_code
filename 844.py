# Title: 844. Backspace String Compare
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        # s = "ab#c" -> after backspace -> ac
        # t = "ad#c" -> after backspace -> ac
        # therefore, they are equal

        # s = "a#c" -> after backspace       -> c
        # t = "b"   -> there is no backspace -> b
        # therefore, they are not equal
        def build_string_after_backspace(v: str):
            # this is easy version not O(1) space
            result = []
            for c in v:
                # since it is backspace, we need to pop from element from the stack.
                # we guard it len(result) > 0 so that we cannot pop if the result is empty
                if c == '#' and len(result) > 0:
                    result.pop()
                else:
                    # we just append to the stack
                    result.append(c)
            return ''.join(result)

        return build_string_after_backspace(s) == build_string_after_backspace(t)


#### test

#### case 1
solution = Solution()
s = "ab#c"
t = "ad#c"
result = solution.backspaceCompare(s, t)
assert result

#### case 2
solution = Solution()
s = "ab##"
t = "c#d#"
result = solution.backspaceCompare(s, t)
assert result

#### case 3
solution = Solution()
s = "a#c"
t = "b"
result = solution.backspaceCompare(s, t)
assert not result
