import sys
import math
import time
import random

swapp = 0
compp = 0

#Random Array generator

def random_arr():
    start_rand_arr = []
    for i in range(100):
        random_number = random.randint(1, 100)
        start_rand_arr.append(random_number)
    return start_rand_arr


#SELECTION SORT

def find_min(arr):
    len_arr = len(arr)
    minimum = 101
    minimum_pos = None
    global compp
    for i in range(len_arr):
        compp += 1
        if arr[i] < minimum:
            minimum = arr[i]
            minimum_pos = i
    return minimum_pos

def Selection_Sort(arr, reverse = True):
    for i in range(len(arr)):
        x = find_min(arr[i:])
        swap(arr, i, x+i)
    if reverse:
        arr.reverse()
        return arr
    else:
        return arr

def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]
    global swapp
    swapp += 1

#INSERTION SORT

def Insertion_Sort(arr, reverse = True):
    len_arr = len(arr)
    global compp
    global swapp
    for i in range(1,len_arr):
        insert = arr[i]
        j = i-1
        while (j >= 0 and arr[j] > insert):
            compp += 1
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = insert
        swapp +=1
    if reverse:
        arr.reverse()
        return arr
    else:
        return arr

#SHELL SORT

def knuth(len_arr):
    h = 1
    while h < len_arr:
        h = 3*h + 1
    h = h//9
    return h

def Shell_Sort(arr, reverse = True):
    len_arr = len(arr)
    gap = knuth(len_arr)
    global compp
    global swapp
    while gap > 0:
        for i in range(gap, len_arr):
            insert = arr[i]
            j = i
            while(j >= gap and arr[j-gap] > insert):
                compp += 1
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = insert
            swapp += 1
        gap //= 3
    if reverse:
        arr.reverse()
        return arr
    else:
        return arr


## BASIC ##


print("Give me an array pls:")
array = input().split()
try:
    array = list(map(int, array))
except ValueError:
    print("Array must contain valid Values")


start_random_array = random_arr()
start_time = time.perf_counter()

print("Starting input array:", array)
#print("Sorted input array:", Selection_Sort(array, reverse=False))
#print("Sorted input array:", Insertion_Sort(array, reverse=False))
#print("Sorted input array:", Shell_Sort(array, reverse=False))
print("I have done:", swapp, "swaps")
print("I have done:", compp, "comparisons")
swapp, compp = 0, 0
print("Starting randomized array:", start_random_array)
#print("Sorted randomized array:", Selection_Sort(start_random_array, reverse=False))
#print("Sorted randomized array:", Insertion_Sort(start_random_array, reverse=False))
#print("Sorted randomized array:", Shell_Sort(start_random_array, reverse=False))
print("I have done:", swapp, "swaps")
print("I have done:", compp, "comparisons")
print("It took me:", time.perf_counter() - start_time, "seconds to run")

#TEST CASE
#45 63 44 90 14 56 49 34 37 52 57 81 76 6 74 87 19 2 69 13 58 91 70 82 11 51 100 31 55 84 18 96 8 98 92 15 94 93 75 64 83 9 12 66 65

#SORTED TEST CASE
#[2, 6, 8, 9, 11, 12, 13, 14, 15, 18, 19, 31, 34, 37, 44, 45, 49, 51, 52, 55, 56, 57, 58, 63, 64, 65, 66, 69, 70, 74, 75, 76, 81, 82, 83, 84, 87, 90, 91, 92, 93, 94, 96, 98, 100]