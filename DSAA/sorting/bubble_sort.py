def bubble_sort(list, iteration):
    iteration = iteration + 1
    print "Iteration:", iteration
    n = len(list)
    i = 0;
    swapped = False
    comparisons = 0
    while i < n - iteration:
        print list
        j = i + 1
        comparisons = comparisons + 1
        if list[i] > list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
            swapped = True
        i = i + 1
    print "List: ", list
    if swapped:
        bubble_sort(list, iteration)

if __name__ == '__main__':
    iteration = 0
    list = [1,8,4,6,9,3,5,2,7,0]
    #list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print list
    bubble_sort(list, 0)
    print list
