def selection_sort(L):
    n = len(L)
    for i in range(n - 1):
        max_j = 0
        for j in range(n - i):
            if L[j] > L[max_j]:
                max_j = j
        if (n - i - 1) != max_j:
            L[n - i - 1], L[max_j] = L[max_j], L[n - i - 1]
    
    return L

def selection_sort_reverse(L):
    n = len(L)
    for i in range(n - 1):
        min_j = 0
        for j in range(n - i):
            if L[j] < L[min_j]:
                min_j = j

        if min_j != n - i - 1:
            L[n - i - 1], L[min_j] = L[min_j], L[n - i - 1]
        
    return L
