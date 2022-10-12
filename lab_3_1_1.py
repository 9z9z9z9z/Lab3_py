
def reducer(tupler):
    m = int(tupler[0])  # Числитель
    n = int(tupler[1])  # Знаменатель
    nod = 1
    if m > n:
        print("Invalid argument")
    else:
        for i in range(2, m + 1):
            if m % i == 0 and n % i == 0:
                nod = i
    return (m / nod, n / nod)


if __name__ == "__main__":
    print(reducer((4, 100)))
