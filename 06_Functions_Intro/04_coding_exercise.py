def  sum_eo(n, t):
    total = 0
    if "e" in t:
        start = 2
    elif "o" in t:
        start = 1
    else:
        return -1

    for i in range(start, n, 2):
        total += i
    return total


x = sum_eo(11, 'spam')
print(x)