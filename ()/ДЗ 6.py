def bubble_sort(arr):
    N = 5000
    ResultOk = False
    First = 0
    Last = N-1
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

unsorted_list = [66, 39, 25, 16, 48, 11, 95]
print("Cписок:", unsorted_list)

sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

target = 25
index = binary_search(sorted_list, target)
if index != -1:
    print(f"Элемент {target} найден на позиции {index}.")
else:
    print(f"Элемент {target} не найден.")
