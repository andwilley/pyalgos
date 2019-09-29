from collections import deque

class Solution:
    def nextClosestTime(self, time: str) -> str:
        # you'll always have a 0, 1 or 2 in the mix
        # you'll always have a number between 0-5 inclusive


        # 19:34
        #   look for the next number higher than 4, use that as the last digit
        #   19:39

        # 19:39
        #   look for a number higher than 9, doesn't exist
        #   set the current digit to the lowest number
        #   19:31
        #   look for a number just higher than 3 but less than 6, doesn't exist
        #   set current digit to lowest number
        #   19:11
        #   look for number higher than 9, doesn't exist
        #   set current digit to lowest number
        #   11:11
        #   start with numbers here that make the time greater than previous, so 2
        #   if no number like the above and less than 3 exists, use lowest number
        #   11:11

        # 23:59
        #   23:52
        #   23:22
        #   22:22

        # 18:39
        #   23:32
        #   23:22
        #   22:22

        # edge case for the hours ones digit, we need to make sure if we pick a number greater than orig, that it works with the tens digit

        def make_new_time(old_time, next_time):
            i = 4 - len(next_time)
            whole_time = [str(x) for x in old_time[:i] + list(next_time)]
            return ':'.join([''.join(whole_time[0:2]), ''.join(whole_time[2:4])])

        def get_next_unique_in_rotation(dgts, dgts_srtd, element, limit=9):
            i = dgts_srtd.index(element)
            for d in dgts_srtd[i:] + dgts_srtd[:i]:
                if d != element and d <= limit:
                    return (d, d > element)
            return (element, False)

        digits = [int(x) for x in list(time.replace(':', ''))]
        digits_sorted = sorted(digits)
        next_time = deque([])

        # minutes ones digit
        m_ones = get_next_unique_in_rotation(digits, digits_sorted, digits[3])
        next_time.appendleft(m_ones[0])
        if m_ones[1]:
            return make_new_time(digits, next_time)

        # minutes tens digit
        m_tens = get_next_unique_in_rotation(digits, digits_sorted, digits[2], 5)
        next_time.appendleft(m_tens[0])
        if m_tens[1]:
            return make_new_time(digits, next_time)

        # hours ones digit
        if digits[0] == 2:
            limit = 3
        else:
            limit = 9
        h_ones = get_next_unique_in_rotation(digits, digits_sorted, digits[1], limit)
        next_time.appendleft(h_ones[0])
        if h_ones[1]:
            return make_new_time(digits, next_time)

        # hours tens digit
        h_tens = get_next_unique_in_rotation(digits, digits_sorted, digits[0], 2)
        next_time.appendleft(h_tens[0])
        return make_new_time(digits, next_time)

