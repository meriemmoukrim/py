


def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid

        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return "malqithash"


myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = int(input("elach katqaleb"))

result = binarySearch(myArray, myTarget)

if result != "malqithqsh":
    print("Value", myTarget, "found at index", result)
else:
    print("Target not found in array.")