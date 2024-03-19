from utils import generate_random_integers, clear_cmd
import random

clear_cmd()

# Selection Sort
print('''
####### Quick Sort ######
1. Choose random pivot
2. Split into two arrays: 
   left: items smaller than pivot
   right: items larger than pivot
3. merge including pivot
Most implementations are not stable
Time complexity: worst case - O(n2), best case - O(n log n)
Space complexity: worst case - O(n), best case - or O(log n)
''')

def quick_sort(array, order = "asc"):
    if not array or len(array) <= 1:
        return array
    
    left_arr = []
    right_arr = []
    random_idx = random.randint(0, len(array) - 1)
    pivot = array.pop(random_idx)

    for elem in array:
        if order == "asc":
            if elem <= pivot:
                left_arr.append(elem)
            if elem > pivot:
                right_arr.append(elem)
        if order == "desc":
            if elem >= pivot:
                left_arr.append(elem)
            if elem < pivot:
                right_arr.append(elem)

    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)


if __name__ == "__main__":
    array = generate_random_integers(0, 1000, 15)
    array.extend(array[9:])
    print(array, '\n')
    sorted_array = quick_sort(array)
    print(sorted_array)