
"""
Selection Sort Algorithm : Sorts a given array by selection sort
Input: An array data[0..n − 1] has some elements
Output: Array data[0..n − 1] sorted in ascending order

"""

def selection_sort(data):
    array_len = len(data)
    for i in range(array_len):
        min_index = i
        for j in range(i+1, array_len):
            if data[j] < data[min_index]:
                min_index = j
        #Swaps data[i] , data[min_index] when current index i not same as min_index index
        if min_index != i:
            data[i] , data[min_index] = data[min_index] , data[i]

    return data

data = [100,12,90,19,22,8,12]
data2 = [9]
data3 = [10,9,8,7,6,5,4,3,2,1]

test_case1 = selection_sort(data)
test_case2 = selection_sort(data2)
test_case3 = selection_sort(data3)

print(test_case1)
print(test_case2)
print(test_case3)

"""
Time Complexity Analysis O(n^2)
Number of swaps in insertion sort is O(n) which distinguish insertion sort positively from other sorting algorithms

"""