# Recursive Binary search
from utils import generate_ordered_integers, clear_cmd

clear_cmd()
print('''
####### Recursive Binary Search ######
Time complexity is 0(logn)
''')

def recursive_binary_search(array, target):
    if len(array) == 0: return False
    mid = len(array) // 2
    if array[mid] == target: return True
    if array[mid] > target:
        return recursive_binary_search(array[:mid], target)
    if array[mid] < target:
        return recursive_binary_search(array[mid:], target)

if __name__ == "__main__":
    items = generate_ordered_integers(33, 70)
    target_item = 25

    print(items)
    print(f"\n{target_item} position is:\n{recursive_binary_search(items, target_item)}\n")