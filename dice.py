# count the number of times numbers appear on top (or bottom)
# whatever the smallest number of occurrances of the bottom number, or zero occurences,
# use that number to turn all the dice to.
# turning dice, add 1 if the number we're turning to is not on bottom, 2 if it is.
# we go through the array 2ce, O(n)


# it also matters what is showing up...
# if we also count the number of times something is face up..., which is just the recip of the other one
# we should turn to the number with the biggest diff between its face up and its recip count

from collections import Counter

"""Find the minimum "turns" to get all dice on same value

Parameters:
    dice_array -- [int] -- the list of face up dice values

Returns:
    int -- the minimum number of turns required
"""
def turn_dice(dice_array):
    face_up_count = Counter() # face down can be derived from this
    # with this
    recip = lambda x: 7 - x
    # set all to 0 initially
    for x in range(1, 7):
        face_up_count[x] = 0
    # count the occurances of each value
    for die in dice_array:
        face_up_count[die] += 1
    ratio_to_recip = Counter()
    # find the largest difference between a number and its recip
    for x in range(1, 7):
        ratio_to_recip[x] = face_up_count[x] - face_up_count[recip(x)]
    # use the largest difference as the number to turn to
    turn_to = ratio_to_recip.most_common(1)[0]
    turns = 0
    # turn the dice, 2 if its the recip facing up, 1 if not the value, 0 if it matches the value
    for die in dice_array:
        if die == recip(turn_to[0]):
            turns += 2
        elif die != turn_to[0]:
            turns += 1
    return turns
