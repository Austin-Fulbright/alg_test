def merge(left, right):
    merge_a = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            merge_a.append(left[i])
            i+=1
        else:
            merge_a.append(right[j])
            j+=1
    if i < len(left):
        merge_a.extend(left[i:])
    if j < len(right):
        merge_a.extend(right[j:])
    return merge_a

def mergesort(array):
    if len(array) <= 1:
        return array
    m = len(array) // 2
    left = mergesort(array[:m])
    right = mergesort(array[m:])

    return merge(left, right)

def evenSubsetMax(nums):
    numsSorted = mergesort(nums)
    maxnum = 0
    current = 0
    for i in range(len(nums)):
        current+=numsSorted[i]
        if (i + 1) % 2 == 0:
            maxnum = max(current, maxnum)
    return maxnum

