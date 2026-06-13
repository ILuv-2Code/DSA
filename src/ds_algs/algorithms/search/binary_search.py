def binary_search(target, L):
    return _bs_search(target, L, 0, len(L) - 1)

def _bs_search(target, L, left, right):
    if left > right:
        return False
    
    mid = (left + right) // 2

    if L[mid] == target:
        return True

    elif L[mid] > target:
        return _bs_search(target, L, left, mid - 1)

    else:
        return _bs_search(target, L, mid + 1, right)

def binary_search_iterative(L, item):
    left, right = 0, len(L)
    
    while right - left > 1:
        mid = (right + left) // 2

        if item < L[mid]:
            right = mid

        else:
            left = mid
    return right > left and L[left] == item