
#
# Binary search algorithm
#

def binary_search(list, item):
    # Low is declared as the first element of the array
    low = 0
    # High is declared as the last element of the array
    high = len(list)-1

    # We will use high and low to control witch part of the array is being search

    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 24, 28, 43, 75]

print(binary_search(my_list, 2))
print(binary_search(my_list, -300))
