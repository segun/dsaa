def merge_sort(list):
    if len(list) == 1:
        return list

    mid = len(list)/2
    left = merge_sort(list[0:mid])
    right = merge_sort(list[mid:])

    sorted = merge(left, right);
    print "sorted: ", sorted

    return sorted


def merge(l1, l2):
    print l1, ", ", l2
    nl = [];
    while(l1 and l2):
        if(l1[0] > l2[0]):
            nl.append(l2[0])
            l2.remove(l2[0])
        else:
            nl.append(l1[0])
            l1.remove(l1[0])
    if l1:
        nl += l1

    if l2:
        nl += l2

    return nl

list = [44, 10, 14, 31, 19, 26, 33, 35, 42, 27, 2, 9, 88, 3, 3, 4, 14, 5, 35, 7, 1]
merge_sort(list)
