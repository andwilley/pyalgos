class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        """
        could define a stack that takes these letters in order.
        if it gets a letter out of order, it returns false
        if it gets one it can add, it returns true

        then we have a list of those stacks and we try each one.
        if it can't be inserted into any stack, we make a new stack if its a c.
        if it can't be inserted and its not a c, fail


        Edge: any letter not 'croak'

        optimizations:
            - space, we're making a stack for every letter, we could probably use less space here
                - maybe first step is removing full stacks
                - not using a stack is probably the next step (think indexes)
            - time, we go through the stacks we don't necessaryily need to

        **optimized:**

        dict with c r o a k as keys
        represents the number of stacks that end in that letter
        for each letter
        if letter is c, increment c
        else check the dict for the previous letter,
        if the prev letter in not 0, increment the letter itself and decrement the previous
        solution is the max sum of all values in the dict if sum is 0 at the end
        if not 0, solution is -1
        """
        lookup_prev = {
            'r': 'c',
            'o': 'r',
            'a': 'o',
            'k': 'a',
        }

        stacks = {
            'c': 0,
            'r': 0,
            'o': 0,
            'a': 0,
        }

        simul_stacks = 0
        for char in croakOfFrogs:
            if char == 'c':
                stacks[char] += 1
            elif char != 'k' and stacks[lookup_prev[char]] > 0:
                stacks[lookup_prev[char]] -= 1
                stacks[char] += 1
            else:
                stacks[lookup_prev[char]] -= 1
            simul_stacks = max([simul_stacks, sum(stacks.values())])

        return simul_stacks if sum(stacks.values()) == 0 else -1
