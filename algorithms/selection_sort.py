from utils import generate_random_integers, clear_cmd

clear_cmd()

# Selection Sort
print('''
####### Selection Sort ######
1. Find the minimum
2. Swap or append to an array/list
Swapping creates unstable sort
Time complexity: worst case - O(n2), best case - O(n)
Space complexity: stable - O(n) or O(1), unstable - O(1)
''')

def selection_sort(main_list, order = "desc"):
    sub_list = []

    while main_list:
        target = find_target(main_list, order)
        main_list.remove(target)
        sub_list.append(target)

    return sub_list

# Find min or max based on ASC or DESC order
def find_target(items, order):
    target = items[0]
    for i in range(1, len(items)):
        # Ascending
        if order == "asc" and target > items[i]:
            target = items[i]
        # Descending
        if order == "desc" and target < items[i]:
            target = items[i]
    return target


if __name__ == "__main__":
    array = generate_random_integers(0, 1000, 15)
    array.extend(array[9:])
    print(array, '\n')
    sorted_array = selection_sort(array)
    print(sorted_array)


