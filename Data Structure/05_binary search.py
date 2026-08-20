def binary_search(list, objective, start, end ):
    if start > end:
        return -1
    center = (start + end) // 2
    if list[center] == objective:
        return center
    elif list[center] < objective:
        return binary_search(list, objective, center + 1, end)
    else:
        return binary_search(list, objective, start, center - 1)
# Example of use
list = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 15, 20, 27, 34, 39, 50]
objective = 27
start_search = 0
end_search = len(list) - 1

result = binary_search(list, objective, start_search, end_search)

if result != -1:
    print(f"The number {objective} is in position: {result}.")
else:
    print(f"The number {objective} is NOT in the list")
