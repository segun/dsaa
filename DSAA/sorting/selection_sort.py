def selection_sort(list, old_min_index):
    min_index = find_min_index(list, old_min_index)
    temp = list[old_min_index]
    list[old_min_index] = list[min_index]
    list[min_index] = temp
    if old_min_index + 1 < len(list):
        selection_sort(list, old_min_index + 1)

def find_min_index(list, from_index):
    n = len(list)
    i = from_index
    min = list[i]
    min_index = i
    while i < n:
        if list[i] < min:
            min = list[i]
            min_index = i
        i = i + 1
    return min_index


if __name__ == '__main__':
    list = [44, 10, 14, 31, 19, 26, 33, 35, 42, 27, 2, 9, 88, 3, 3, 4, 14, 5, 35, 7, 1]
    selection_sort(list, 0)
    print list
