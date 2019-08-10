input = [
    "and word another word the word",
    "1zj 1 4 34 1 321",
    "3 randome words in here",
    "2 randome words in here",
    "435 how will this work",
    "hxc it might actually work",
    "mn4 whoa, its working",
    "5n3 4 5 7 1 432",
    "5n4 6 5 7 1 432",
    "5n5 99 5 7 1 432",
]

from heapq import heappush, heappop

class Order:
    def __init__(self, log_string):
        words = log_string.split(" ")
        first_meta = words[1]
        self.entire_log = log_string
        self.id = words[0]
        self.meta = log_string[len(self.id) + 1:]
        self.is_prime = not first_meta.isdigit()

    def __lt__(self, other):
        if self.meta != other.meta:
            return self.meta < other.meta
        return self.id < other.id

def organize_logs(orders):
    prime_orders = []
    other_orders = []

    # list for each, order the primes by lex
    for order in orders:
        order_obj = Order(order)
        if order_obj.is_prime:
            heappush(prime_orders, order_obj)
        else:
            other_orders.append(order)

    # reassemble the list:
    final_list = []
    while prime_orders:
        final_list.append(heappop(prime_orders).entire_log)
    return final_list + other_orders
