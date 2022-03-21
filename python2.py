def counts(list, set):
    dictionary = dict.fromkeys(set,0)
    for val in set:
        dictionary[val] = list.count(val)
    return dictionary
    
x = [4, -2, 3, 9, 4, 17, 5, 29, 14, 87, 4, -2, 100]
y = [-2, 4, 29]
print(counts(x,y))

def switch_pairs(StringOne):
    stringTwo = '' 
    for i in range(0, len(StringOne), 2): 
        if(i+1 < len(StringOne)): 
            stringTwo += StringOne[i + 1] + StringOne[i]
        else:
            stringTwo += StringOne[i]
    return stringTwo

print(switch_pairs("example"))
print(switch_pairs("hello there"))
print(switch_pairs("homework"))