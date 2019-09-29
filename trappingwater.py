class Solution:
    def trap(self, height: List[int]) -> int:
        unclosed = [] # [(index, top, bottom)]
        last = 0
        res = 0

        for i, h in enumerate(height):
            if h > last:
                # check the unclosed array ...
                # no need to check the entire array, just pop until there aren't any more or
                # h isn't above the bottom of the drop
                # handle the case where h is above the bottom, but below the top
                # (change the bottom and append back to the unclosed list)
                while unclosed and h > unclosed[-1][2]: # bottom element
                    closed = unclosed.pop()
                    if h < closed[1]:
                        # it only closes some of these heights
                        # (curr index - old index - 1) * (current height - old bottom)
                        res += (i - closed[0] - 1) * (h - closed[2])
                        # re-add that unclosed to the array, with a bottom just above current height
                        unclosed.append((closed[0], closed[1], h))
                    else:
                        # it closes the whole thing
                        res += (i - closed[0] - 1) * (closed[1] - closed[2])
            if h < last:
                # add to the unclosed array...
                unclosed.append((i - 1, last, h))
            last = h
        return res