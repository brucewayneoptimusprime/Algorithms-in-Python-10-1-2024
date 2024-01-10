def quicksort_last_pivot(arr, start, end):
    if start < end:
        choose_last_pivot(arr, start, end)  # Exchange the pivot element with the last element
        partition_index = partition(arr, start, end)

        comparisons = end - start
        comparisons += quicksort_last_pivot(arr, start, partition_index - 1)
        comparisons += quicksort_last_pivot(arr, partition_index + 1, end)

        return comparisons
    else:
        return 0

def choose_last_pivot(arr, start, end):
    # Exchange the last element with the first element
    arr[start], arr[end] = arr[end], arr[start]

def partition(arr, start, end):
    pivot = arr[start]
    i = start + 1

    for j in range(start + 1, end + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[start], arr[i - 1] = arr[i - 1], arr[start]
    return i - 1

def main():
    with open('E:/quicksort.txt', 'r') as file:
        array = [int(line.strip()) for line in file]

    comparisons = quicksort_last_pivot(array, 0, len(array) - 1)
    print(f"Total comparisons: {comparisons}")

if __name__ == "__main__":
    main()
