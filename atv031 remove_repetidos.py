def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l
    

#def numeric_compare(x, y):
 #   return x - y
#sorted([5, 2, 4, 1, 3], cmp=numeric_compare)
#[1, 2, 3, 4, 5]


#def reverse_numeric(x, y):
 #   return y - x
#sorted([5, 2, 4, 1, 3], cmp=reverse_numeric)
#[5, 4, 3, 2, 1]