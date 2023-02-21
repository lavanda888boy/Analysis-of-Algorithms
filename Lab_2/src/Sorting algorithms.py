import numpy as np
from random import randint
from time import time
from matplotlib import pyplot as plot

# function to merge two sorted partition arrays 
# and the main merge sort function itself
def merge(arr, lower, mid, upper):
    n1 = mid - upper + 1
    n2 = lower - mid
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[lower + i]
 
    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]
 
    i = 0
    j = 0 
    k = lower 
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
 
def mergeSort(array, lowerBound, upperBound):
    if lowerBound < upperBound:
        middle = lowerBound + (upperBound - lowerBound) // 2
 
        mergeSort(array, lowerBound, middle)
        mergeSort(array, middle + 1, upperBound)
        merge(array, lowerBound, middle, upperBound)



# function for finding pivot element in an array
# and the main quick sort function      
def partition(arr, lower, upper):
    index = randint(lower, upper)
    pivot = arr[index]

    i = lower - 1

    for j in range(lower, upper):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
 
    (arr[i + 1], arr[upper]) = (arr[upper], arr[i + 1])
 
    return i + 1
 
 
def quickSort(array, lowerBound, upperBound):
    if lowerBound < upperBound:
        pivot = partition(array, lowerBound, upperBound)
        quickSort(array, lowerBound, pivot - 1)
        quickSort(array, pivot + 1, upperBound)


# helper function to modify heap
# and the heap sort main function itself
def heapify(arr, n, i):
    root = i
    left = 2 * i + 1
    right = 2 * i + 2
  
    if left < n and arr[i] < arr[left]:
        root = left
  
    if right< n and arr[root] < arr[right]:
        root = right
  
    if root != i:
        (arr[i], arr[root]) = (arr[root], arr[i])
        heapify(arr, n, root)

  
def heapSort(array):
    n = len(array)
  
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
  
    for i in range(n - 1, 0, -1):
        (array[i], array[0]) = (array[0], array[i])
        heapify(array, i, 0)


# function for shell sort implementation
def shellSort(array, n):
    gap = n // 2
      
    while gap > 0:
        j = gap

        while j < n:
            i = j - gap
              
            while i >= 0:
                if array[i + gap] > array[i]:
                    break
                else:
                    (array[i + gap], array[i]) = (array[i], array[i + gap])
  
                i = i - gap
            j += 1

        gap = gap // 2


# testing all the algorithms
def current_time_millis():
    return time() * 1000


integer_constant = 1000
size_of_array = 5000

iteration_list = list()

merge_list = list()
quick_list = list()
heap_list = list()
shell_list = list()

for index in range(0, 6):
    iteration_list.append(size_of_array)

    test_array = np.random.randint(-integer_constant, integer_constant, size=size_of_array)
    copy_array = test_array

    start_time = current_time_millis()
    mergeSort(test_array, 0, size_of_array - 1)
    end_time = current_time_millis()
    merge_list.append(round(end_time - start_time, 4))

    copy1_array = copy_array

    start_time = current_time_millis()
    quickSort(copy_array, 0, size_of_array - 1)
    end_time = current_time_millis()
    quick_list.append(round(end_time - start_time, 4))

    copy2_array = copy1_array

    start_time = current_time_millis()
    heapSort(copy1_array)
    end_time = current_time_millis()
    heap_list.append(round(end_time - start_time, 4))

    start_time = current_time_millis()
    shellSort(copy2_array, size_of_array)
    end_time = current_time_millis()
    shell_list.append(round(end_time - start_time, 4))

    size_of_array *= 2


# plotting the obtained results
plot.figure()

plot.plot(iteration_list, merge_list, color="red", label="Merge sort")
plot.plot(iteration_list, quick_list, color="blue", label="Quick sort")
plot.plot(iteration_list, heap_list, color="green", label="Heap sort")
plot.plot(iteration_list, shell_list, color="black", label="Shell sort")
plot.title("Sorting algorithms", color="violet", fontsize=16)

plot.legend(loc='upper left')

plot.xlabel("n", color="violet", fontsize=14)
plot.ylabel("T(millis)", color="violet", fontsize=14)

plot.grid()
plot.show()
