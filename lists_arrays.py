# Assignment 4: Lists / Arrays in Python

def sum_elements(arr):
    total = 0
    for x in arr:
        total += x
    return total

def average_elements(arr):
    return sum_elements(arr) / len(arr) if len(arr) > 0 else 0

def find_index(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

def contains_value(arr, value):
    for x in arr:
        if x == value:
            return True
    return False

def remove_element(arr, value):
    result = []
    removed = False
    for x in arr:
        if x == value and not removed:
            removed = True
            continue
        result.append(x)
    return result

def copy_list(arr):
    result = []
    for x in arr:
        result.append(x)
    return result

def insert_at(arr, index, value):
    result = []
    for i in range(len(arr) + 1):
        if i == index:
            result.append(value)
        if i < len(arr):
            result.append(arr[i])
    return result

def min_max(arr):
    minimum = maximum = arr[0]
    for x in arr:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return minimum, maximum

def reverse_list(arr):
    result = []
    i = len(arr) - 1
    while i >= 0:
        result.append(arr[i])
        i -= 1
    return result

def duplicate_elements(arr):
    duplicates = []
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count > 1 and not contains_value(duplicates, arr[i]):
            duplicates.append(arr[i])
    return duplicates

def count_even_odd(arr):
    even = odd = 0
    for x in arr:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

def common_elements(a, b):
    result = []
    for x in a:
        if contains_value(b, x) and not contains_value(result, x):
            result.append(x)
    return result

def remove_duplicates(arr):
    result = []
    for x in arr:
        if not contains_value(result, x):
            result.append(x)
    return result

def second_largest(arr):
    unique = remove_duplicates(arr)
    sorted_arr = sort_without_builtin(unique)
    return sorted_arr[-2] if len(sorted_arr) >= 2 else None

def difference_max_min(arr):
    minimum, maximum = min_max(arr)
    return maximum - minimum

def contains_12_and_23(arr):
    return contains_value(arr, 12) and contains_value(arr, 23)

def unique_elements_only(arr):
    result = []
    for x in arr:
        count = 0
        for y in arr:
            if x == y:
                count += 1
        if count == 1:
            result.append(x)
    return result

def frequency_count(arr):
    freq = {}
    for x in arr:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    return freq

def sort_without_builtin(arr):
    result = copy_list(arr)
    for i in range(len(result)):
        for j in range(0, len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

def merge_without_duplicates(a, b):
    result = []
    for x in a + b:
        if not contains_value(result, x):
            result.append(x)
    return result

if __name__ == "__main__":
    arr = [12, 5, 23, 7, 5, 9, 23, 30]
    arr2 = [5, 40, 12, 50]
    print("Sum:", sum_elements(arr))
    print("Average:", average_elements(arr))
    print("Index of 23:", find_index(arr, 23))
    print("Contains 9:", contains_value(arr, 9))
    print("Remove 5:", remove_element(arr, 5))
    print("Copy:", copy_list(arr))
    print("Insert 100 at index 2:", insert_at(arr, 2, 100))
    print("Min and Max:", min_max(arr))
    print("Reverse:", reverse_list(arr))
    print("Duplicates:", duplicate_elements(arr))
    print("Even and Odd Count:", count_even_odd(arr))
    print("Common:", common_elements(arr, arr2))
    print("Remove Duplicates:", remove_duplicates(arr))
    print("Second Largest:", second_largest(arr))
    print("Difference Max-Min:", difference_max_min(arr))
    print("Contains 12 and 23:", contains_12_and_23(arr))
    print("Unique Elements Only:", unique_elements_only(arr))
    print("Frequency:", frequency_count(arr))
    print("Sorted:", sort_without_builtin(arr))
    print("Merged without duplicates:", merge_without_duplicates(arr, arr2))
