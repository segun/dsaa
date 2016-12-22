def insertion_sort(to_sort, iteration):
    iteration = iteration + 1
    n = len(to_sort)
    i = 0
    while i < n - 1:
        j = i + 1
        if to_sort[i] > to_sort[j]:
            #swap
            print "Swapping: ", to_sort[i], to_sort[j]
            temp = to_sort[i]
            to_sort[i] = to_sort[j]
            to_sort[j] = temp
            sort_down(to_sort, 0, j)
        i = i + 1

def sort_down(to_sort, low, n):
    i = n
    while i > low:
        j = i - 1
        print to_sort
        if to_sort[i] < to_sort[j]:
            #swap
            temp = to_sort[i]
            to_sort[i] = to_sort[j]
            to_sort[j] = temp
        i = i - 1

if __name__ == "__main__":
    l = [4,6,3,2,1,9,7]
    insertion_sort(l, 0)
    print l
