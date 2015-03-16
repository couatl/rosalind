def maj(elements):
    maj_candidate = elements[0]
    count = 0
    for element in elements:
        if element == maj_candidate:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_candidate = element
            count = 1
    return maj_candidate if elements.count(maj_candidate) > len(elements)/2 else -1
