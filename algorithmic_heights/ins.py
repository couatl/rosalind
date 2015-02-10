def number_of_swap_in_insertion_sort(a):
    number_of_swap = 0
    for i in xrange(1, len(a)):
        k = i
        while k >= 1 and a[k] < a[k-1]:
            a[k-1], a[k] = a[k], a[k-1]
            k -= 1
            number_of_swap += 1
    return number_of_swap
