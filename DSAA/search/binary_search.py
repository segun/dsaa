def binary_search(x, list, low, high):
    if low > high:
        return -1
    mid = low + (high - low) / 2
    if x > list[mid]:
        low = mid + 1
        return binary_search(x, list, low, high)
    elif x < list[mid]:
        high = mid - 1
        return binary_search(x, list, low, high)
    elif x == list[mid]:
        return mid


if __name__ == "__main__":
    l = [1,2,3,4,5,6,7]
    pos = binary_search(2, l, 0, 6)
    print "X found at position: ", pos
