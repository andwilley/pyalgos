"""
1  2  3  4  5
0  1  2  3  4
"""

tickets = [1, 4, 6, 7, 8]
t2 = [2, 2, 10, 10]

def calc_best_per_num_tickets(tickets):
    best_prices = {}
    for i, ticket in enumerate(tickets):
        min_value = ticket
        index = i
        while index > i / 2:
            index -= 1
            new_value = best_prices[index + 1] + best_prices[i - index]
            min_value = min(min_value, new_value)
        best_prices[i + 1] = min_value
    return best_prices

def get_best_price(tickets, num_tickets):
    prices = calc_best_per_num_tickets(tickets)
    print(prices)
    return prices[num_tickets]

print(get_best_price(t2, 4))
