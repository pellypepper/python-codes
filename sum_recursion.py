def sum_recursion(arr, index):
    """
    a functio that takes a list and an index, 
    it returns the sum of the elements of the array up to the index
    """
  
    if index == 0: # base case
        return arr[0]
    else:
        # recursive case
        return arr[index] + sum_recursion(arr, index - 1) 
   

arr = [4,3,1,5]
index = 1
print(sum_recursion(arr, index))