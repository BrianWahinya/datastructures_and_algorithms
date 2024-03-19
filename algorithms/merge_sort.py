from utils import generate_random_integers, clear_cmd

clear_cmd()

# Merge Sort
print('''
####### Merge Sort ######
Time complexity is 0(n log n)
''')

def merge_sort(arr):

    if len(arr) <= 1: return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return merge(left, right)

def merge(left, right):
    merged = []
    idx_left = idx_right = 0

    while idx_left < len(left) and idx_right < len(right):
        if left[idx_left] < right[idx_right]:
            merged.append(left[idx_left])
            idx_left += 1
        else:
            merged.append(right[idx_right])
            idx_right += 1

    merged.extend(left[idx_left:])
    merged.extend(right[idx_right:])

    return merged

if __name__ == "__main__":
    array = generate_random_integers(0, 1000, 15)
    sorted_array = merge_sort(array)
    print(array, '\n')
    print(sorted_array)