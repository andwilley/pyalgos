def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # start in the middle of the smaller array
    # so start = 0, end = len(small) - 1
    # small_position = (start + end) / 2
    # position to start in larger array is:
    # (small.length + large.length + 1)/2 - small_position

    # check if:
    # maxleftsmall <= minrightlarge
    # and maxleftlarge <= minrightsmall
    # if this is true, we found the median
    # watch the edge case where one list doesn't overlap at all with the other (use inf)
    # return the avg( max(minleftsmall, minleftlarge), min(minrightsmall, minrightlarge) ) if odd
    # or max(minleftsmall, minleftlarge) if even

    # if that check isn't true
    # and maxleftsmall > minrightlarge
    # make end = small_position - 1
    # start over

    # else make end = small_position + 1
    # start over
