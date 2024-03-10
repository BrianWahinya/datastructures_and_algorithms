from utils import generate_unordered_integers, clear_cmd

clear_cmd()

# Linear search
print('''
####### Linear Search ######
Time complexity is 0(n)
''')

def linear_search(array, target):
    for i, item in enumerate(array):
        if item == target:
            return i
    return None

if __name__ == "__main__":
    items = generate_unordered_integers(1, 20)
    target_item = 7
    
    print(items)
    print(f"\n{target_item} position is:\n{linear_search(items, target_item)}\n")