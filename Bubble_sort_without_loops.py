def bubble_sort(arr):
    if len(arr) <=1:
        return arr
    if len(arr) == 2:
        return arr if arr[0] < arr[1] else [arr[1],arr[0]]

    a,b = arr[0],arr[1]
    bs = arr[2:]
    res = []

    if a<b:
        res = [a] + bubble_sort([b]+bs)
    else:
        res = [b] + bubble_sort([a] + bs)
    return bubble_sort(res[:-1]) + res[-2:]

arr = [1,3,4,5,6,2]
res=bubble_sort(arr)
print(*res)