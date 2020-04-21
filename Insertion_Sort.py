"""
Insertion Sort is not fast algorithm because it uses nested loops to sort
it can be used only for small data

Check below image for more illustration about how insertion sort works
https://github.com/hesham9090/Algorithms/blob/master/images/InsertionSort.png



"""

data = [100,12,90,19,22,8,12]
data2 = [9]
data3 = [10,9,8,7,6,5,4,3,2,1]

def insertion_sort(data):

   for j in range(1, len(data)):
       key = data[j]
       i = j - 1
       while (i >= 0) and (data[i] > key):
           data[i + 1] = data[i]
           i = i - 1
       data[i + 1] = key
   return data

test_case1 = insertion_sort(data)
test_case2 = insertion_sort(data2)
test_case3 = insertion_sort(data3)
print(test_case1)
print(test_case2)
print(test_case3)

"""
Time Complexity Analysis O(n^2)
"""
