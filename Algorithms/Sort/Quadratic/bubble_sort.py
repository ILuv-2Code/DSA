# O(n^2) time
# O(1) space

def bubble_sort_ascending(L):
    n = len(L)
    for iteration in range(n):
        swapped = False
        for element in range(0, n - iteration - 1):
            if L[element] > L[element+1]:
                swapped = True
                L[element], L[element+1] = L[element+1], L[element]
        if not swapped:
            break
    return L

def bubble_sort_descending(L):
    n = len(L)
    for iteration in range(n):
        swapped = False
        for element in range(0, n - iteration - 1):
            if L[element] < L[element+1]:
                swapped = True
                L[element], L[element+1] = L[element+1], L[element]
        if not swapped:
            break
    return L