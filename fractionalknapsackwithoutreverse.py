def sort_by_value(item):
    return item[0]
def sort_by_weight(item):
    return item[1]
def sort_by_ratio(item):
    return item[0]/item[1]
def fractional_knapsack(w,items,strategy='ratio'):
    if strategy=='value':
        items.sort(key=sort_by_value,reverse=True)
    elif strategy=='weight':
        items.sort(key=sort_by_weight)
    elif strategy=='ratio':
        items.sort(key=sort_by_ratio,reverse=True)
    total_value=0.0
    result_items=[]
    for value, weight in items:
        if w==0:
            break
        if weight<=w:
            total_value+=value
            w-=weight
            result_items.append((value,weight,1.0))
        else:
            fraction=w/weight
            total_value+=value*fraction
            result_items.append((value,weight,fraction))
            w=0
    print(strategy.upper())
    print(total_value)
    print("Item taken(value,weight,fraction):")
    for v,w,f in result_items:
        print(f"value{v},weight:{w},fraction:{f}")
    return total_value
items=[(5,1),(10,3),(15,5),(7,4),(8,1),(9,3),(4,2)]
w=15
print(fractional_knapsack(w,items.copy(),'value'))
print(fractional_knapsack(w,items.copy(),'weight'))
print(fractional_knapsack(w,items.copy(),'ratio'))