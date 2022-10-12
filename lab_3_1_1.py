
def reducer(tupler):
    m = int(tupler[0])  # Числитель
    n = int(tupler[1])  # Знаменатель
    nod = 1
    if m > n or m < 0 or n <= 0:
        print("Invalid argument")
    else:
        for i in range(2, m + 1):
            if m % i == 0 and n % i == 0:
                nod = i
    return (m / nod, n / nod)


print(reducer((4, 100)))
