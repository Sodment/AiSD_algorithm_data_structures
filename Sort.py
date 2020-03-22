import sys
import math
import time
import random
sys.setrecursionlimit(10**9)


swapp = 0
compp = 0

# Random Array generator

def random_arr():
    start_rand_arr = []
    for i in range(100):
        random_number = random.randint(1, 100)
        start_rand_arr.append(random_number)
    return start_rand_arr

# Swap 2 elements of a list, not really useful as i used it max 2 times

def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]
    global swapp
    swapp += 1

# SELECTION SORT #

def find_min(arr):
    len_arr = len(arr)
    minimum = 99999
    minimum_pos = None
    global compp
    for i in range(len_arr):
        compp += 1
        if arr[i] < minimum:
            minimum = arr[i]
            minimum_pos = i
    return minimum_pos

def Selection_Sort(arr, reverse=True):
    for i in range(len(arr)):
        x = find_min(arr[i:])
        swap(arr, i, x+i)
    if reverse:
        arr.reverse()
        return arr
    else:
        return arr


# INSERTION SORT #

def Insertion_Sort(arr, reverse=True):
    len_arr = len(arr)
    global compp
    global swapp
    for i in range(1,len_arr):
        insert = arr[i]
        j = i-1
        while (j >= 0 and arr[j] > insert):
            compp += 1
            arr[j+1] = arr[j]
            swapp += 1
            j = j-1
        arr[j+1] = insert
        swapp += 1
    if reverse:
        arr.reverse()
        return arr
    else:
        return arr

# SHELL SORT #


def knuth(len_arr):
    h = 1
    while h < len_arr:
        h = 3*h + 1
    h = h//9
    return h

def Shell_Sort(arr, reverse=True):
    len_arr = len(arr)
    gap = knuth(len_arr)
    global compp
    global swapp
    while gap > 0:
        for i in range(gap, len_arr):
            insert = arr[i]
            j = i
            while(j >= gap and arr[j-gap] > insert):
                arr[j] = arr[j-gap]
                j -= gap
                compp += 1
            arr[j] = insert
            swapp += 1
        knuth_growth.append(gap)
        gap //= 3
    if reverse:
        arr.reverse()
        return arr
    else:
        return arr


# HEAP SORT #

def Max_Heapify(arr, n, i):
    global compp
    global swapp
    largest = i
    left = (2 * i) + 1
    right = (2 * i) + 2
    if left < n and arr[left] > arr[i]:
        largest = left
        compp += 1
    if right < n and arr[right] > arr[largest]:
        largest = right
        compp += 1
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        swapp += 1
        Max_Heapify(arr, n, largest)

def Build_Max_Heap(arr):
    len_arr = len(arr)
    for i in range((len_arr//2), -1, -1):
        Max_Heapify(arr, len_arr, i)
    return arr

def Heap_Sort(arr, reverse=True):
    n = len(arr)
    Build_Max_Heap(arr)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        Max_Heapify(arr, i, 0)
    if reverse:
        arr.reverse()
        return arr
    else:
        return arr


# Merge Sort

def Merge_Sort(arr):
    global compp
    global swapp
    n = len(arr)
    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]

        Merge_Sort(left)
        Merge_Sort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                arr[k] = left[i]
                swapp += 1
                i += 1
                compp += 1
            else:
                arr[k] = right[j]
                swapp += 1
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            swapp += 1
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            swapp += 1
            j += 1
            k += 1
    return arr

# QUICK SORT

def Quick_Sort(arr, p, r):
    global compp
    global swapp
    if p > r:
        q = Partition(arr, p, r)
        Quick_Sort(arr, p, q-1)
        Quick_Sort(arr, q+1, r)
    return arr
def Partition(arr, p, r):
    global compp
    global swapp
    x = arr[r]
    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            swapp += 1
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1






## DRIVER CODE ##

while True:
    print("PLease decide from what source you want me to read data:")
    print("Write \"txt\" to read from Sort.txt file")
    print("Write \"keyboard\" to read from keyboard")
    type_of_action = input()
    if type_of_action == "keyboard":
        print("Give me an array pls:")
        array = input().split()
        try:
            array = list(map(int, array))
            break
        except ValueError:
            print("Array must contain valid values")
    elif type_of_action == "txt":
        a = open("Sort.txt","r")
        a = a.read()
        array = a.split()
        try:
            array = list(map(int, array))
            break
        except ValueError:
            print("Array must contain valid values")
    else:
        print("Please, try again")
        continue

start_random_array = random_arr()
start_time = time.perf_counter()

# STARTING OUTPUT #

print("Starting input array:", array)

print("Input array sorted by Selection Sort:", Selection_Sort(array, reverse=True))
print("I have done:", swapp, "swaps")
print("I have done:", compp, "comparisons")
swapp, compp = 0, 0

print("Input array sorted by Insertion Sort:", Insertion_Sort(array, reverse=True))
print("I have done:", swapp, "swaps")
print("I have done:", compp, "comparisons")
swapp, compp = 0, 0

knuth_growth = []
print("Input aarray sorted by Shell Sort:", Shell_Sort(array, reverse=True))
if knuth_growth:
    print("Knuths growth:", end=' ')
    for i in range(len(knuth_growth)):
        print(knuth_growth[i], end=' ')
    print()
print("I have done:", swapp, "swaps")
print("I have done:", compp, "comparisons")
swapp, compp = 0, 0

print("Input array sorted by Heap Sort:", Heap_Sort(array, reverse=True))
print("I have done:", swapp, "swaps")
print("I have done:", compp, "comparisons")
swapp, compp = 0, 0

print("Input array sorted by Merge Sort:", Merge_Sort(array))

print("Input array sorted by Quick Sort:", Quick_Sort(array, 0, len(array)-1))
'''if pivot:
    print("Pivots:", end=' ')
    for i in range(len(pivot)):
        print(pivot[i], end=' ')
    print()'''
print("I have done:", swapp, "swaps")
print("I have done:", compp, "comparisons")
swapp, compp = 0, 0


# RANDOM ARRRAY OUTPUT #

print("Starting randomized array:", start_random_array)
print("Randomized array sorted by Selection Sort:", Selection_Sort(start_random_array, reverse=True))
print("I have done:", swapp, "swaps")

print("I have done:", compp, "comparisons")
swapp, compp = 0, 0

print("Randomized array sorted by Insertion Sort:", Insertion_Sort(start_random_array, reverse=True))
print("I have done:", swapp, "swaps")

print("I have done:", compp, "comparisons")
swapp, compp = 0, 0

knuth_growth = []
print("Randomized array sorted by Shell Sort:", Shell_Sort(start_random_array, reverse=True))
if knuth_growth:
    print("Knuths growth:", end=' ')
    for i in range(len(knuth_growth)):
        print(knuth_growth[i], end=' ')
    print()

print("I have done:", swapp, "swaps")

print("I have done:", compp, "comparisons")
swapp, compp = 0, 0

print("Randomized array sorted by Heap Sort:", Heap_Sort(start_random_array, reverse=True))
print("I have done:", swapp, "swaps")

print("I have done:", compp, "comparisons")
swapp, compp = 0, 0

print("Input array sorted by Merge Sort:", Merge_Sort(start_random_array))

print("Input array sorted by Quick Sort:", Quick_Sort(start_random_array, 0, len(array)-1))
'''if pivot:
    print("Pivots:", end=' ')
    for i in range(len(pivot)):
        print(pivot[i], end=' ')
    print()'''
print("I have done:", swapp, "swaps")
print("I have done:", compp, "comparisons")
swapp, compp = 0, 0

print("It took me:", time.perf_counter() - start_time, "seconds to run")

# TEST CASE
# 45 63 44 90 14 56 49 34 37 52 57 81 76 6 74 87 19 2 69 13 58 91 70 82 11 51 100 31 55 84 18 96 8 98 92 15 94 93 75 64 83 9 12 66 65

# SORTED TEST CASE
# 2, 6, 8, 9, 11, 12, 13, 14, 15, 18, 19, 31, 34, 37, 44, 45, 49, 51, 52, 55, 56, 57, 58, 63, 64, 65, 66, 69, 70, 74, 75, 76, 81, 82, 83, 84, 87, 90, 91, 92, 93, 94, 96, 98, 100