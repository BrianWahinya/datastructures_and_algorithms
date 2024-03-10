# Binary search
from utils import generate_ordered_integers, clear_cmd

clear_cmd()
print('''
####### Binary Search ######
Time complexity is 0(logn)
''')

def binary_search(array, target):
    first_idx = 0
    last_idx = len(array) - 1

    while first_idx <= last_idx:
        middle_idx = (first_idx + last_idx) // 2
        middle_item = array[middle_idx]

        if array[first_idx] == target:
            return first_idx
        
        if array[last_idx] == target:
            return last_idx

        if middle_item < target:
            first_idx = middle_idx + 1

        elif middle_item > target:
            last_idx = middle_idx - 1

        else:
            return middle_idx
    
    return None

if __name__ == "__main__":
    items = generate_ordered_integers(33, 50)
    target_item = 35

    print(items)
    print(f"\n{target_item} position is:\n{binary_search(items, target_item)}\n")