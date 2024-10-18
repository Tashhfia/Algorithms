# best case = O(n)
# worst case = O(n^2)

# not good for large datasets
# less steps than bubble sort

ins = [1,6,7,4,2,9,8,5,3]

for curr_index in range(1, len(ins)):
    temp = ins[curr_index]
    prev_index = curr_index - 1

    while(prev_index>= 0 and temp < ins[prev_index]):
        ins[prev_index + 1] = ins[prev_index]
        prev_index = prev_index - 1
    
    ins[prev_index + 1] = temp
    
print(ins)