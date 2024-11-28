def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    n = len(a[0])
    m = len(b)
    if n!=m:
        return -1
    c = []
    for i in a:
        temp = 0
        for j in range(len(i)):
            temp += i[j] * b[j]
        c.append(temp)  
    return c