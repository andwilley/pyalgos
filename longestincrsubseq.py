from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # for each number in nums
        # search for it in the incr array
        # if the index == len: put it at the end
        # else put it at the index
        # return the length of the incr array

        # the way to see this is to build a tree (or several)
        # each time we see a number, see if its greater than an existing node in a tree
        # then add it to the last node its greater than
        # make a new tree if its less than all the roots
        # you end up with a tree (or several) that represents all the possible combination of
        # increasing numbers you could have
        # you'll see that you only need to keep the lowest number at every level
        # which goes from being a huge marass of tree
        # to a single array, where we can replace items at equal levels
        # and since its sorted, we can use binary search to insert it

        increasing = [0] * len(nums)
        incr_len = 0

        for num in nums:
            i = bisect_left(increasing, num, 0, incr_len)
            increasing[i] = num
            if i == incr_len:
                incr_len += 1

        return incr_len