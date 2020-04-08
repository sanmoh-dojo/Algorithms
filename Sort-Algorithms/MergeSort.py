def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def mergeSort(list):
    if len(list) < 2:
        return list

    middle = len(list) / 2
    left = mergeSort(list[:middle])
    right = mergeSort(list[middle:])

    return merge(left, right)


def mergeSortRecursive(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSortRecursive(L)
        mergeSortRecursive(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i])


arr = [12, 11, 13, 5, 6, 7]
print("Sorted Array is : ")

# For Recusive
# mergeSortRecursive(arr)
# printList(arr)

# For Iterative
print(mergeSort(arr))
