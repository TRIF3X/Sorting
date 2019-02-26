### recursive sorting function
def merge_sort( arr ):

    # Checks to see if the array is current longer than 1 element
    if len(arr) > 1:
        # mid is the length of the array divided by 2 rounded down using //
        mid = len(arr) // 2
        # left half of the array is the array from 0 to the mid variable
        left = arr[:mid]
        # right half of the array is the array from the mid variable to the end
        right = arr[mid:]

        # Recursively call merge_sort until everything is divided into 1
        merge_sort(left)
        merge_sort(right)


    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort( arr, low, high ):

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
