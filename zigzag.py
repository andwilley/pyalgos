'''
This works for increasing or decreasing the numbers. the challenge said decrease only.
'''

def movesToMakeZigzag(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2:
        return 0

    penalty = {
        "evenFix": {
            "eHi": 0,
            "oHi": 0
        },
        "oddFix": {
            "eHi": 0,
            "oHi": 0
        }
    }

    for i in range(len(nums)):

        isEven = i%2 == 0
        fix = "evenFix" if isEven else "oddFix"

        prevVal = nums[i - 1] if i > 0 else nums[i]
        nextVal = nums[i + 1] if i < len(nums) - 1 else nums[i]

        leftDiff = prevVal - nums[i]
        rightDiff = nextVal - nums[i]
        posDiff = abs(max(leftDiff, rightDiff))
        negDiff = abs(min(leftDiff, rightDiff))
        maxDiff = max(abs(leftDiff), abs(rightDiff))

        isZag = leftDiff * rightDiff > 0 # this one is good for either evens or odds, whatever it is
        if (i == 0 or i == len(nums) - 1) and maxDiff != 0:
            isZag = True

        # if one is good, add penalty to make the opposite case
        if isZag:
            if leftDiff > 0 or rightDiff > 0: # in most cases, they both are the same, except for array ends
                penalty[fix]['eHi' if isEven else 'oHi'] += maxDiff + 1
            else:
                penalty[fix]['oHi' if isEven else 'eHi'] += maxDiff + 1
        else:
            penalty[fix]['eHi'] += posDiff + 1 if isEven else negDiff + 1
            penalty[fix]['oHi'] += posDiff + 1 if not isEven else negDiff + 1

    return min(penalty["evenFix"]['eHi'], penalty["evenFix"]['oHi'],
                penalty["oddFix"]['eHi'], penalty["oddFix"]['oHi'])

# for just decreasing...
def movesToMakeZigzagActual(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 1:
        return 0

    penalty = {
        "evenFix": 0,
        "oddFix": 0
    }

    for i in range(len(nums)):

        # for each item
        # add the cost of making it lower than its neighbors to the odd/even variable

        fix = "evenFix" if i%2 == 0 else "oddFix"

        # find the diff between neighbors, if begin or end, set the non-existant one to equal the opposite one
        prevVal = nums[i - 1] if i > 0 else nums[i + 1]
        nextVal = nums[i + 1] if i < len(nums) - 1 else nums[i - 1]

        leftDiff = prevVal - nums[i]
        rightDiff = nextVal - nums[i]
        maxNegDiff = abs(min(leftDiff, rightDiff))

        needsToDecrease = leftDiff <= 0 or rightDiff <= 0

        penalty[fix] += maxNegDiff + 1 if needsToDecrease else 0

    return min(penalty["evenFix"], penalty["oddFix"])