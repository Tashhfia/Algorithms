def mergeSort(a):
# to stop when we have 1 element
    if (len(a) < 2):
        return a
    # split down the middle
    mid = len(a) // 2
    # split till we are left with only one elements in each side
    left = mergeSort(a[:mid])
    right = mergeSort(a[mid:])

# merge both sides
    return merge(left, right, a) 
 
def merge(left, right, a):
    sorted_list = []
    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # if we run out of right elements
    while i < len(left):
        sorted_list.append(left[i])
        i+=1
    # if we run out of left elements
    while j < len(right):
        sorted_list.append(right[j])
        j+=1
    
    return sorted_list

if __name__ == "__main__":
    ins = [1,6,7,4,2,9,8,5,3]
    print(mergeSort(ins))