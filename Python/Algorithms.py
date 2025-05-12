import random
import time

#
# CHATGPT MADE THIS
#
class SortingAlgorithms:

    def merge_sort(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left_half = SortingAlgorithms.merge_sort(lst[:mid])
        right_half = SortingAlgorithms.merge_sort(lst[mid:])
        return SortingAlgorithms.merge(left_half, right_half)

    def merge(left, right):
        sorted_lst = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_lst.append(left[i])
                i += 1
            else:
                sorted_lst.append(right[j])
                j += 1
        sorted_lst.extend(left[i:])
        sorted_lst.extend(right[j:])
        return sorted_lst

    def quick_sort(lst, low, high):
        if low < high:
            pi = SortingAlgorithms.partition(lst, low, high)
            SortingAlgorithms.quick_sort(lst, low, pi - 1)
            SortingAlgorithms.quick_sort(lst, pi + 1, high)

    def partition(lst, low, high):

        mid = (low + high) // 2
        lst[mid], lst[high] = lst[high], lst[mid]  
        pivot = lst[high]

        i = low - 1
        for j in range(low, high):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        return i + 1


# 
# Test scenarios
# 
# def compare_performance():
#     original_sorted_list = list(range(10000))
#     original_reversed_list = list(range(10000, 0, -1))
#     original_random_list = random.sample(range(1, 10001), 10000)

#     for name, lst in [("Sorted", original_sorted_list),
#                       ("Reversed", original_reversed_list),
#                       ("Random", original_random_list)]:
#         lst_copy = lst.copy()
#         start_time = time.time()
#         SortingAlgorithms.merge_sort(lst_copy)
#         print(f"Merge Sort - {name} list: {time.time() - start_time:.6f} seconds")

#         lst_copy = lst.copy()
#         start_time = time.time()
#         SortingAlgorithms.quick_sort(lst_copy, 0, len(lst_copy) - 1)
#         print(f"Quick Sort - {name} list: {time.time() - start_time:.6f} seconds")
# compare_performance()

# def test_sorting_edge_cases():
#     edge_cases = {
#         "Empty list": [],
#         "Single element": [42],
#         "Duplicates": [5, 3, 8, 3, 9, 5, 3]
#     }

#     for case, lst in edge_cases.items():
#         ms_result = SortingAlgorithms.merge_sort(lst.copy())
#         qs_list = lst.copy()
#         SortingAlgorithms.quick_sort(qs_list, 0, len(qs_list) - 1)
#         print(f"{case} - Merge Sort: {ms_result}, Quick Sort: {qs_list}")
# test_sorting_edge_cases()