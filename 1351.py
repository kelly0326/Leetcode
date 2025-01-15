def negative_num_list(lst):
    count = 0
    for num in lst:
        if num < 0:
            count += 1
    # print(count)
    return count
# print(negative_num_list(lst))

def main():
    sum = 0
    for item in grid:
        # print(item)
        # print(negative_num_list(item))
        sum = sum + negative_num_list(item)
    # return negative_num_list(item)
    print(sum)
    return sum
return main()
