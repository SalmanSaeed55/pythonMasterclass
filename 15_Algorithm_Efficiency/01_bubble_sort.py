def bubble_sort(data):
    n = len(data)
    comparison_count = 0

    for i in range(n - 1):
        for j in range(n - 1):
            comparison_count += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

        print(f"End of pass {i}\nData is now:\n\t{data}")
    print(comparison_count)


numbers = [3, 2, 4, 1, 5, 7, 6]
print(f"Sorting {numbers}")
bubble_sort(numbers)
print(f"Sorted Data:\t {numbers}")

bubble_sort(list(range(70, 2, -4)))
