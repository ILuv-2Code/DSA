def merge_sort(L):
    if len(L) < 2:
        return L

    mid = len(L)//2
    A = L[:mid]
    B = L[mid:]

    merge_sort(A)
    merge_sort(B)

    _merge(A, B, L)
    return L

def _merge(A, B, L):
    i = 0
    j = 0

    while (i < len(A)) and (j < len(B)): 
        if A[i] < B[j]:
            L[i+j] = A[i]
            i += 1
        else:
            L[i+j] = B[j]
            j += 1
    
    L[i+j:] = A[i:] + B[j:]