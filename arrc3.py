def quicksort_median_of_three(arr, start, end):
    if start < end:
        choose_median_of_three_pivot(arr, start, end)  # Choose the median-of-three pivot
        partition_index = partition(arr, start, end)

        comparisons = end - start
        comparisons += quicksort_median_of_three(arr, start, partition_index - 1)
        comparisons += quicksort_median_of_three(arr, partition_index + 1, end)

        return comparisons
    else:
        return 0

def choose_median_of_three_pivot(arr, start, end):
    mid = (start + end) // 2
    candidates = [(arr[start], start), (arr[mid], mid), (arr[end], end)]

    # Find the median among the three candidates
    median_value, median_index = sorted(candidates)[1]

    # Exchange the median element with the first element
    arr[start], arr[median_index] = arr[median_index], arr[start]

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

    comparisons = quicksort_median_of_three(array, 0, len(array) - 1)
    print(f"Total comparisons: {comparisons}")

if __name__ == "__main__":
    main()
