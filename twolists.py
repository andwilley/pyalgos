fwd = [[1, 8], [2, 9], [3, 14]]
rtrn = [[1, 1], [2, 7], [3, 10], [4, 18]]

fwd4 = [[1, 8], [2, 9], [3, 10]]
rtrn4 = [[1, 1], [5, 3], [2, 7], [3, 10], [4, 18]]

fwd3 = [[1, 7], [2, 7], [3, 7]]
rtrn3 = [[1, 7], [2, 7], [3, 7], [4, 7]]

fwd2 = []
rtrn2 = [[1,2], [2, 4]]

def get_max_pairs(fwd, rtrn, max):

    if not fwd or not rtrn:
        return [[]]

    # O(nlogm)
    fwd = sorted(fwd, key=lambda x: x[1])
    # O(nlogn)
    rtrn = sorted(rtrn, key=lambda x: x[1], reverse=True)

    best_routes = []
    best_dist = 0

    # worst case, O(n^2), but unless most of the values are the same
    # we stop the search if we can't ever beat the max
    # we also stop if we exceed the limit
    for rtrn_route in rtrn:
        # don't keep decrementing rtrn array if we can't beat the best distance
        if rtrn_route[1] + fwd[-1][1] < best_dist:
            break;
        for fwd_route in fwd:
            sum = fwd_route[1] + rtrn_route[1]
            pair = [fwd_route[0], rtrn_route[0]]
            # don't increment the fwd array if we go over the max
            if sum > max:
                break;
            if not best_routes or sum == best_dist:
                best_routes.append(pair)
                best_dist = sum
            elif sum > best_dist:
                best_routes = [pair]
                best_dist = sum

    return best_routes if best_routes else [[]]

print(get_max_pairs(fwd3, rtrn3, 15))
