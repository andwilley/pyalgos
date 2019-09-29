from random import random

class Item:
    def __init__(self, val, weight):
        self.val = val
        self.weight = weight

    def __repr__(self):
        return f"<Item: val: {self.val}, weight: {self.weight}>"

collection = [Item("A", 1), Item("B", 2), Item("C", 1)]

def normalize_weights(collection):
    sum = 0
    for item in collection:
        sum += item.weight

    prev_val = 0
    cumm_val = 0
    for item in collection:
        item.weight, prev_val = (prev_val / sum) + cumm_val, item.weight
        cumm_val = item.weight

    return collection

def weighted_choice(collection):
    res_index = None
    if not collection:
        raise ValueError("Must contain a value")
    collection = normalize_weights(collection)
    choice = random()
    for index, item in enumerate(collection):
        if item.weight >= choice:
            res_index = index - 1
            break;
    return collection[res_index].val if res_index != None else collection[-1].val

print(weighted_choice(collection))
