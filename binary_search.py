
#
# Binary search algorithm ~ Python
#
# GitHub repo: https://github.com/Alex-G-R/Binary-search
# Creator GitHub profile: https://github.com/Alex-G-R
#

# Let's define our function
def binary_search(list, item):
    # Low is declared as the first element of the array.
    low = 0
    # High is declared as the last element of the array.
    high = len(list)-1

    # We will use high and low to control witch part of the array is being search.

    # Until the search filed won't be sized down to 1 element...
    while low <= high:
        # We choose the middle element...
        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid # We found the item!
        if guess > item:
            high = mid - 1 # Our guess is too high
        else:
            low = mid + 1 # Our guess is too low
    return None # Provided item doesn't exist, return None

# With binary search our list MUST be sorted! 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 24, 28, 43, 75]
# Index    0, 1, 2, 3, 4, 5, 6, 7, 8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 => end of the list.


print(binary_search(my_list, 2)) # This will print 1, remember that the first element has the index of 0, second the index of 1 and so on...

print(binary_search(my_list, -300)) # The item we provided doesn't exist in my_list, this will return None.
