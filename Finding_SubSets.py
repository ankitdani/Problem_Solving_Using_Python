import null as null


def all_subsets(arr):
    subset = [arr.length]
    # subset = new int[arr.length]
    helper(arr, subset, 0)


def helper(arr, subset, i):
    print("test")
    if i == arr.length:
        print(subset)
    else:
        subset[i] = null
        helper(arr, subset, i + 1)
        subset[i] = arr[i]
        helper(arr, subset, i + 1)


if __name__ == '__main__':
    n = int(input("Enter the total number of elements in the array: "))
    arr = []
    for i in range(0, n):
        arr.append(int(input()))
    print(arr)
    all_subsets(arr)
