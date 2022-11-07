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
            print(*tmp, sep=" ")
            return None
        else:
            continue
    print(False)
    return None


base = []
tmp_base = input().split()
for i in tmp_base:
    base.append(int(i))

x = int(input())

check(x, base)
