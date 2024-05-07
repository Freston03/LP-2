A = [64, 25, 12, 22, 11]
for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]
 
print ("Sorted array : ")
for i in range(len(A)):
    print("%d" %A[i],end=" ")




# Function for Selection Sort of elements

def Selection_Sort(array):
    for i in range(len(array)):

        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        # Swap the minimum element with the first element
        array[i], array[min_idx] = array[min_idx], array[i]
    

# Main

array=[]
n = int(input("\nEnter number of element in Array : "))

print("\nEnter Elements in Array : ")
for i in range(0, n):
    ele = int(input())
    array.append(ele)  # adding the element

print("\nArray Before Performing Selection Sort : ")
print(array)

print("\nArray After Performing Selection Sort : ")
Selection_Sort(array)
print(array)


# Here's a step-by-step explanation of the selection sort algorithm:

# Start with an unsorted array of n elements.
# Find the minimum (or maximum) element in the unsorted part of the array.
# Swap the minimum (or maximum) element with the first element of the unsorted part.
# Move the boundary of the sorted part one element to the right.
# Repeat steps 2-4 until the entire array is sorted.