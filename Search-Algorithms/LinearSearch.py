def search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return True
    return False


array = [1, 2, 'Test', 4, 'Test 2', 6]
key = 'Test'

if search(array, key):
    print("Found")
else:
    print("Not Found")
