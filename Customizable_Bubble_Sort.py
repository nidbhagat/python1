def bubble_sort(lst, comparison_func):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if comparison_func(lst[j], lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

def is_greater(a, b):
    return a > b

def max_comparisons_bubble_sort(n, k):
    return n * (n - 1) // 2 - (n - k) * (n - k - 1) // 2

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list, is_greater)
print("Sorted list:", my_list)

n = 8
k = 3
max_comparisons = max_comparisons_bubble_sort(n, k)
print("Max comparisons:", max_comparisons)
