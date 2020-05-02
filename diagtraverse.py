from collections import deque

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        self.nums = nums
        res = []

        """
        until the last row
        for each row
            curr_brt = max(0, (curr_row_len - 1) - (num_rows - 1 - curr_row_index))
            max_brt = max(max_brt, curr_brt)
            grab the first number
            then until row == -1,
                traverse row-1, col+1 and grab each number


        optimize:
        - we know the index in the new array that each item will land at
        - create a new list for each row
        - for each item in each row
         - new_row_index = col_index + row_index
         - append left to new_row
        - concat new_rows
        """

        res = []
        for i, row in enumerate(nums):
            for j, col_val in enumerate(row):
                new_row_index = i + j
                if new_row_index > len(res) - 1:
                    res.append(deque([]))
                res[new_row_index].appendleft(col_val)

        return [x for l in res for x in l]

    def naive(self):
        def back_up(start_row_i, start_col_i, res):
            if start_row_i <= 0:
                return res
            col_i = start_col_i
            for row_i in range(start_row_i - 1, -1, -1):
                col_i += 1
                self.append_safe(res, row_i, col_i)
            return res


        max_brt = 0
        for row_i, row in enumerate(nums):
            curr_brt = max(0, (len(row) - 1) - (len(nums) - 1 - row_i))
            max_brt = max(max_brt, curr_brt)
            self.append_safe(res, row_i, 0) # mutates res
            back_up(row_i, 0, res)

        for col_i in range(1, max_brt + 1):
            self.append_safe(res, len(nums) - 1, col_i)
            back_up(len(nums) - 1, col_i, res)

        return res


    def append_safe(self, res, row_i, col_i):
        if row_i > len(self.nums) - 1 or col_i > len(self.nums[row_i]) - 1:
            return res
        else:
            return res.append(self.nums[row_i][col_i])

