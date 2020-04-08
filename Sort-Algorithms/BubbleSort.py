def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def recursiveBubbleSort(arr):
    for i, num in enumerate(arr):
        try:
            if arr[i + 1] < num:
                arr[i] = arr[i + 1]
                arr[i + 1] = num
                recursiveBubbleSort(arr)
        except IndexError:
            pass
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]

recursiveBubbleSort(arr)
print ("Sorted array is : ")
for i in range(len(arr)):
    print ("%d" % arr[i])
