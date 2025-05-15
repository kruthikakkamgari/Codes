def by_value(item):
    return -item[0]
def by_weight(item):
    return item[1]
def by_ratio(item):
    return -item[0]/item[1]
def fractional(capacity,items,strategy='ratio'):
    if strategy=='value':
        items.sort(key=by_value)
    elif strategy=='weight':
        items.sort(key=by_weight)
    else:
        items.sort(key=by_ratio)
    total_profit=0.0
    for value,weight in items:
        if capacity==0:
            break
        if weight<=capacity:
            total_profit+=value
            capacity-=weight
        else:
            total_profit+=value*(capacity/weight)
            break
    return total_profit
items=[(5,1),(10,3),(15,5),(7,4),(8,1),(9,3),(4,2)]
w=15
print(fractional(w,items.copy(),'value'))
print(fractional(w,items.copy(),'weight'))
print(fractional(w,items.copy(),'ratio'))