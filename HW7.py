def bubbleSort(array):
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

#data = [-2, 45, 0, 11, -9]

#bubbleSort(data)

#print('Sorted Array:')
#print(data)

def binarySearch(array, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return x
#array = [3, 4, 5, 6, 7, 8, 9]
#x = 7
#print(binarySearch(array, x, 0, len(array)-1))




