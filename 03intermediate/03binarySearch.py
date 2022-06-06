'''
ITERATIVE APPROACH
'''

def binary_search(arr , val):
    low=0
    high = len(arr) -1 

    while low <=high:
        mid = low + ((high-low)//2)

        if arr[mid] < val :
            low = mid + 1

        elif arr[mid] > val:
            high = mid -1

        elif arr[mid] == val :
            return mid
        else:
            return -1


# TODO : RECURSIVE 

def binary_helper(arr, low ,high , val):
    if low > high :
        return -1
    mid = low + ((high-low)//2)

    if arr[mid] > val :
        binary_helper(arr , low , mid -1 ,val)
    elif arr[mid] < val :
        binary_helper(arr , mid+1 , high ,val)
    else:
        return mid


def rec_binary(arr,val):
    return binary_helper(arr , 0 , len(arr)-1 , val)