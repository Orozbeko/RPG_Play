def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def binary_search(element, arr):
    arr = sorted(arr)
    first = 0
    last = len(arr) - 1
    result_ok = False

    while first <= last and not result_ok:
        mid = (first + last) // 2
        if arr[mid] == element:
            result_ok = True
        elif arr[mid] < element:
            first = mid + 1
        else:
            last = mid - 1

    if result_ok:
        print(f"Элемент {element} найден в списке.")
    else:
        print(f"Элемент {element} не найден в списке.")



unsorted_list = [64, 25, 12, 22, 11, 47]
sorted_list = selection_sort(unsorted_list)
print("Отсортированный список (метод выбором сортировки):", sorted_list)

unsorted_list = [64, 25, 12, 22, 11, 47]
sorted_list = selection_sort(unsorted_list)
print("Отсортированный список (метод сортировки выбором):", sorted_list)

element_to_find = 22
my_list = [11, 12, 22, 25, 47, 64]
binary_search(element_to_find, my_list)
