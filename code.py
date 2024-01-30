import time
import random
import matplotlib.pyplot as plt

# Code for Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Code for Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Code Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Code for Benchmarking function
def benchmark_sort(sort_func, array):
    start_time = time.time()
    sort_func(array)
    end_time = time.time()
    return end_time - start_time

# Testing with various input sizes
input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000]  # Extend as needed

# This will Collect data for plotting
insertion_times = []
selection_times = []
bubble_times = []

for size in input_sizes:
    array = random.sample(range(size * 10), size)  # Generate random array
    time_insertion = benchmark_sort(insertion_sort, array.copy())
    time_selection = benchmark_sort(selection_sort, array.copy())
    time_bubble = benchmark_sort(bubble_sort, array.copy())
    insertion_times.append(time_insertion)
    selection_times.append(time_selection)
    bubble_times.append(time_bubble)

# Plotting
plt.plot(input_sizes, insertion_times, label='Insertion Sort')
plt.plot(input_sizes, selection_times, label='Selection Sort')
plt.plot(input_sizes, bubble_times, label='Bubble Sort')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds) : ')
plt.title('The Sorting Algorithm Benchmark is')
plt.legend()
plt.show()
