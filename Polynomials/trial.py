# print("Enter the maximum power")
# power=int(input())
# tuple=()
# for i in range (power,0,-1):
#     print("Enter the coefficient of power ",i)
#     coeff=int(input())
#     tuple+=(coeff,)
# print(tuple)
def addpoly(p1, p2):
    for i in range(len(p1)):
        for item in p2:
            if p1[i][1] == item[1]:
                p1[i] = ((p1[i][0] + item[0]), p1[i][1])
                p2.remove(item)
    p3 = p1 + p2
    for item in (p3):
        if item[0] == 0:
            p3.remove(item)
    return sorted(p3)


def multpoly(p1, p2):
    for i in range(len(p1) - 1):
        for item in p2:
            p1[i] = ((p1[i][0] * item[0]), (p1[i][1] + item[1]))
            p2.remove(item)
    return p1


# print(addpoly([(2,1)],[(-2,1)]))

print(multpoly([(1, 1), (-1, 0)], [(1, 2), (1, 1), (1, 0)]))