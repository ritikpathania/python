def merge_sort(l):
    if len(l) <= 1:
        return l
    # Find the middle point and divide it
    middle = len(l) // 2
    left_list = l[:middle]
    right_list = l[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))


# Merge the sorted halves
def merge(left_half, right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res


l = [64, 34, 25, 12, 22, 11, 90]
print()
print(merge_sort(l))
