def insertion_sort_ascending(L):
    n = len(L)
    for i in range(n):
        j = n - i - 1
        while j < n - 1 and L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
            j += 1
    return L

def insertion_sort_descending(L):
    n = len(L)
    for i in range(n):
        j = n - i - 1
        while j < n - 1 and L[j] < L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
            j += 1
    return L