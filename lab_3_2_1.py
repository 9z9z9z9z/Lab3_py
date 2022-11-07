def F(n):
    if n == 0:
        return 1
    else:
        return n - M(F(n - 1))


def M(n):
    if n == 0:
        return 0
    else:
        return n - F(M(n - 1))


def hofstadter_f_m(n):
    n = int(n)
    ans = list()
    for i in range(n):
        tmp = (F(i), M(i))
        ans.append(tmp)
    yield ans


num = int(input("Input number:\n"))
for i in hofstadter_f_m(num):
    print(i)
