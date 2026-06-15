def quick_sort(L):
    _q_s(L, 0, len(L))
    return L

def _q_s(L, left, right):
    if right - left <= 1:
        return None

    pivot = _partition(L, left, right)

    _q_s(L, left, pivot)
    _q_s(L, pivot + 1, right)


def _partition(L, l, r):
    pivot =  r - 1
    r = pivot - 1
    
    while l < r:
        while  L[l] < L[pivot]:
            l+=1 
        while l<r and L[r] >= L[pivot]:
            r-=1
        if l < r:
            L[l], L[r] = L[r], L[l]
    
    if L[l] > L[pivot]:
        L[l], L[pivot] = L[pivot], L[l]
        pivot = l
    
    return pivot