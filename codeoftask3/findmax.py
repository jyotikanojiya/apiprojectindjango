# by using predif function

def find_max_element(arr):
    return max(arr)
print(find_max_element(arr=[1,2,3,4]))

#lambda+max()
array = [4,6,7,3,2,8]
large = max(array,key=lambda x:x)
print("largest element is :",large)

## max arry

def largest(arr, n):
	max = arr[0]
	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)