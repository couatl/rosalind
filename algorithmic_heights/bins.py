a = [10, 20, 30, 40, 50]
b = [40, 10, 35, 15, 40, 20]

def bin_search(arr, el, shift):
    if not arr: return -1
    i = len(arr) >> 1
    if arr[i] > el:
        return bin_search(arr[:i], el, shift)
    if arr[i] < el:
        return bin_search(arr[i+1:], el, shift + i + 1)
    return i + shift

result = [bin_search(a, x, 1) for x in b]
