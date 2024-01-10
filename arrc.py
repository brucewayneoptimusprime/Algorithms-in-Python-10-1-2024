def quicksort(arr, start, end, choose_pivot):
    if start < end:
        pivot_index = choose_pivot(arr, start, end)
        arr[start], arr[pivot_index] = arr[pivot_index], arr[start]  # Move pivot to the beginning
        partition_index = partition(arr, start, end)
        
        comparisons = end - start
        comparisons += quicksort(arr, start, partition_index - 1, choose_pivot)
        comparisons += quicksort(arr, partition_index + 1, end, choose_pivot)
        
        return comparisons
    else:
        return 0

def partition(arr, start, end):
    pivot = arr[start]
    i = start + 1
    
    for j in range(start + 1, end + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[start], arr[i - 1] = arr[i - 1], arr[start]
    return i - 1

def choose_first_pivot(arr, start, end):
    return start

def main():
    with open('E:/quicksort.txt', 'r') as file:
        array = [int(line.strip()) for line in file]

    comparisons = quicksort(array, 0, len(array) - 1, choose_first_pivot)
    print(f"Total comparisons: {comparisons}")

if __name__ == "__main__":
    main()
