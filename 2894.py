def differenceOfSums(self, n: int, m: int) -> int:
    can_divide = []
    can_not_divide = []
    for i in range(n + 1):
        if i % m == 0:
            can_divide.append(i)
        else:
            can_not_divide.append(i)
    print(can_divide)
    print(can_not_divide)
    total = 0
    total1 = 0
    for i in range(len(can_divide)):
        total = total + can_divide[i]
    print(total)
    for i in range(len(can_not_divide)):
        total1 = total1 + can_not_divide[i]
    print(total1)
    return total1 - total