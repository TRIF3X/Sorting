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

        # Keep track of position of left side
        i = 0
        # Keep track of position of right side
        j = 0
        # Keep track of current position of the array we're putting back together
        k = 0

        # while the array on the left and the right is greater than the index 
        while i < len(left) and j < len(right):
            # if the number on the left array at the first position is less than the number on the right at the first position
            if left[i] < right[j]:
                # insert the number at the current position of k in the array
                arr[k] = left[i]
                # incrememnt i by one so that we are now looking at the next available card on the left
                i = i+1
            # perform the opposite operation
            else:
                arr[k] = right[j]
                j = j+1
            # increment k so that the next number inserted into the array is at the position behind the previous inserted number
            k = k+1


        # if everything on the right is already merged we can just merge the left to the array 
        while i < len(left):
            arr[k] = left[i]
            i = i+1
            k = k+1

        # if everything on the left is already merged we can just merge the right to the array
        while j < len(right):
            arr[k] = right[j]
            j = j+1
            k = k+1


    return arr


print(merge_sort([78, 248, 61, 233, 11, 212, 142, 91, 197, 203, 192, 111, 234, 66, 178, 38, 73, 188, 211, 114, 22]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort( arr ):
    # If the length of the array is less than 2 we know its already sorted
    if len(arr) < 2:
        return arr
    else:
        # the pivot will be the last item in the array
        pivot = arr[len(arr) -1 ]
        # partition everything less than or equal the pivot starting from the last index to the beginning of the array
        less = [i for i in arr[:-1] if i <= pivot]
        # partition everything greater than the pivot starting from the last index to the beginning of the array
        greater = [i for i in arr[:-1] if i > pivot ]

        # return recursively quicksort on everything less than the pivot then add the pivot then add everything greater than the pivot recursively
        return quick_sort(less) + [pivot] + quick_sort(greater)

    return arr

arr1 = [78, 248, 61, 233, 11, 212, 142, 91, 197, 203, 192, 111, 234, 66, 178, 38, 73, 188, 211, 114, 22]

print(quick_sort(arr1))

# len(arr) -1 points to the last index because there is 21 numbers but indexes start at 0

#choose pivot
#compare all items to the pivot
    #items smaller than the pivot 
        #swap to the flag's position
        #increment the flag
    #items larger than the pivot stay in place
#swap pivot into it's place (which we've defined with the flag)


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
