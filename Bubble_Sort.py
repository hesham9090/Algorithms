
"""
Bubble Sort

Sorts a given array by bubble sort
Input: An array data[0..n − 1] of orderable elements
Output: Array data[0..n − 1] sorted in ascending order

"""

def bubble_sort(data):
    array_len = len(data)
    for i in range(array_len):
        for j in range(array_len - 1):
            if data[j] > data[j+1]:
                data[j] , data[j + 1] = data[j+1] , data[j]
    return data


data = [100,12,90,19,22,8,12]
data2 = [9]
data3 = [10,9,8,7,6,5,4,3,2,1]


test_case1 = bubble_sort(data)
test_case2 = bubble_sort(data2)
test_case3 = bubble_sort(data3)

print(test_case1)
print(test_case2)
print(test_case3)


"""
Time Complexity Analysis O(n^2)
"""
