arr = [2,3,4,6,8,9,10,11,12]

x = 31

def binarysearcharray(array,x):
    start = 0
    end = len(array)-1
    while start<=end:
        mid = (start+end)//2
        if array[mid] == x:
            return mid
        elif array[mid]<x:
            start = mid + 1
        else:
            end = mid - 1
    return str(x)+" is not in list"

print(binarysearcharray(arr,x))
