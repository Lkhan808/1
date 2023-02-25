def bubble_sort(array):
    n=array
    for i in range(len(n)):
        for j in range(len(n)-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1], n[j]
    return array

data=[12,34,5,87]
print(bubble_sort(data))


def binary_search(x,my_list):
    n = max(my_list)
    result = False
    first = 0
    last = n - 1
    while(first<last):
        mid = (first + last) // 2
        if x == my_list[mid]:
            first = mid
            last = first
            result = True
            pos = mid
        else:
            if x > my_list[mid]:
                first = mid + 1
            else:
                last = mid - 1
    else:
        if result == True:
            print(f' найдено по индексу: {pos}')
        else:
            print(f' не найдено')
dataa=[1,2,3,4,5,6,7,8,9,10]
binary_search(8, dataa)










