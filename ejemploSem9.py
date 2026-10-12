def merge(a, b):
    c = []

    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            c.append(b[0])  
            b.pop(0)         
        else:
            c.append(a[0])   
            a.pop(0)         


    while len(a) > 0:
        c.append(a[0])
        a.pop(0)

    while len(b) > 0:
        c.append(b[0])
        b.pop(0)

    return c


def mergesort(a):
    n = len(a)
    if n <= 1:              
        return a

    mitad = n // 2
    array_one = a[:mitad]   
    array_two = a[mitad:]    

    array_one = mergesort(array_one)
    array_two = mergesort(array_two)

    return merge(array_one, array_two)


numeros = [38, 27, 43, 3, 9, 82, 10]
print("Original:", numeros)
print("Ordenado:", mergesort(numeros))