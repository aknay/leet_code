from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(modified_image, r, c, r_limit, c_limit, old_color, new_color):
            # we need to check the array bound, if exceed, return
            if r >= r_limit or r < 0 or c >= c_limit or c < 0:
                return
            # we need to check that it should be original color so that we can modify it or
            # it should not be new color that we just modified
            if modified_image[r][c] != old_color or modified_image[r][c] == new_color:
                return
            # we just modify in place
            modified_image[r][c] = new_color
            dfs(modified_image, r, c + 1, r_limit, c_limit, old_color, new_color)  # right
            dfs(modified_image, r, c - 1, r_limit, c_limit, old_color, new_color)  # left
            dfs(modified_image, r + 1, c, r_limit, c_limit, old_color, new_color)  # down
            dfs(modified_image, r - 1, c, r_limit, c_limit, old_color, new_color)  # top

        original_color = image[sr][sc]
        row_limit, column_limit = len(image), len(image[0])
        dfs(image, sr, sc, row_limit, column_limit, old_color=original_color, new_color=color)
        return image


#### test

#### case 1
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
s = Solution()
result = s.floodFill(image, sr=sr, sc=sc, color=color)
assert result == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

#### case 2
image = [[0, 0, 0], [0, 0, 0]]
sr = 0
sc = 0
color = 0
s = Solution()
result = s.floodFill(image, sr=sr, sc=sc, color=color)
assert result == [[0, 0, 0], [0, 0, 0]]
