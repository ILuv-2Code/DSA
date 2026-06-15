def quick_select(L, k):
    if not 0 <= k < len(L):
        raise ValueError("k out of range")
    left, right = 0, len(L)

    while left < right:
        pivot = _partition(L, left, right)

        if k < pivot:
            right = pivot
        elif k > pivot:
            left = pivot + 1
        else:
            return L[pivot]
        
def _partition(L, l, r):
    pivot = r - 1
    r = pivot - 1

    while l < r:
        while L[l] < L[pivot]:
            l += 1

        while l < r and L[r] >= L[pivot]:
            r -= 1

        if l < r:
            L[l], L[r] = L[r], L[l]

    if L[l] > L[pivot]:
        L[l], L[pivot] = L[pivot], L[l]
        pivot = l

    return pivot