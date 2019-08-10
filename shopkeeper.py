input = [2, 3, 1, 2, 4, 2]
input2 = [1,2,3,4,5,6,7,8,9]

def calc_total(item_price_list):
    # for each item in the list
    # look at the pending_lowest array to see if this is lower than any of those.
    # for each one its lower than or equal to, put the current value in the array at the index for
    # that value. then delete that item from the array
    # look at the item and add it to the "pending_lowest" array with its index (value, arr_index)

    pending_lowest = []
    subtract_price_by_index = []

    # O(n)
    for _ in range(len(item_price_list)):
        subtract_price_by_index.append(0)

    # (price, price_index)
    for price_index, price in enumerate(item_price_list):
        delete_items = []
        for pending_index, entry in enumerate(pending_lowest):
            if price <= entry[0]:
                subtract_price_by_index[entry[1]] = price
                delete_items.append(entry)
        # O(d) | d is the number of deleted items
        for entry in delete_items:
            pending_lowest.remove(entry)
        pending_lowest.append((price, price_index))
    return sum([price - subtract_price_by_index[index] for index, price in enumerate(item_price_list)]), [i for i, value in enumerate(subtract_price_by_index) if value == 0]

# this is O(1)
def delete(array, index):
    array[index] = array[-1]
    return array[:-1]

print(calc_total(input2))

# 23280666254232