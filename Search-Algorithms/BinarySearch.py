def binarySearch(array, first, last, input):
    if last >= first:
        mid = first + (last - 1)
        if arr[mid] == input:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, first, mid - 1, input)
        else:
            return binarySearch(arr, mid + 1, last, input)
    else:
        return -1


arr = [2, 3, 4, 5, 6, 10, 20]
key = 10

result = binarySearch(arr, 0, len(arr) - 1, key)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")