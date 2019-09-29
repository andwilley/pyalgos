import math

def nth_ugly_number(n: int, a: int, b: int, c: int) -> int:

    def bsearch(target, lo, hi, mults):
        mid = (lo + hi) // 2
        index = get_ugly_index(mid, *mults)
        print(lo, mid, hi, target, index)
        if target - 1 == index:
            return mid
        return bsearch(target, lo, mid, mults) if index > target else bsearch(target, mid + 1, hi, mults)
    ub = min(2*(10**9), min([a, b, c])*n)

    # binary search from 0 to ub, looking for ugly index to == n
    return bsearch(n, 0, ub, [a, b, c])

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def get_ugly_index(num, a, b, c):
    return num // a + num // b + num // c - num // lcm(a, b) - num // lcm(a, c) - num // lcm(b, c) + num // lcm(lcm(a, b), c)

# print(get_ugly_index(1999999984, *[2, 217983653, 336916467]))
print(nth_ugly_number(1000000000, 2, 217983653, 336916467))