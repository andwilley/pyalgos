from collections import deque

def get_close_pairs(forms, window):
    # keep two queues, A and B
    # for each form, add it to the appropriate queue
    # then dequeue all forms that are too old
    # then add every pair of this with each element in opposite queue to the res

    a_q = deque([])
    b_q = deque([])
    res = []
    for form in forms:
        while a_q and form[1] - a_q[0][1] >= window:
            a_q.popleft()
        while b_q and form[1] - b_q[0][1] >= window:
            b_q.popleft()
        if form[0] == "A":
            a_q.append(form)
            res = add_pairs(form, b_q, res)
        else:
            b_q.append(form)
            res = add_pairs(form, a_q, res)
    return res

def add_pairs(form, opp_q, res):
    for opp_form in opp_q:
        res.append((form, opp_form))
    return res

input = [("A", 1),("A", 2),("B", 3),("A", 4),("B", 5),("A", 6)]


print(get_close_pairs(input, 3))

"""

[a1b3, a2b3, a4b3, a4b5, a6b5]

A
a4
a6


B
b5
"""