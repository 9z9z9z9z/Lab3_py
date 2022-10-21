from random import randint


def randomize():
    ans = list()
    size = randint(1, 30)
    for i in range(size):
        ans.append(randint(0, 10))
    return ans


def check(x, base_list):
    for i in range(len(base_list) - 1):
        sum = 0
        tmp = list()
        for j in range(i,len(base_list)):
            if sum < x:
                sum += base_list[j]
                tmp.append(base_list[j])
            else: break
        if sum == x:
            return tmp
        else:
            continue
    return False

base = randomize()
x = int(input("Input X\n"))

print(check(x, [1, 2, 3]))
