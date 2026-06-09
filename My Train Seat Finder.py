seats = [ 1 , 3 , 5 , 7 , 9 , 11, 13 , 15 , 17 , 19 , 21 , 23 , 25  ]
def iterative_binary_search(arr , target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
def recursive_binary_search(arr , low , high , target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, mid + 1, high, target)
    else:
        return recursive_binary_search(arr, low, mid - 1, target)
seat_number = int(input("Enter the seat number you want to find: "))
result1 = iterative_binary_search(seats, seat_number)
result2 = recursive_binary_search(seats, 0, len(seats) - 1, seat_number)
if result1 != -1:
    print(f"Iterative Binary Search: Seat {seat_number} found at index {result1}.")
else:
    print(f"Iterative Binary Search: Seat {seat_number} not found.")
if result2 != -1:
    print(f"Recursive Binary Search: Seat {seat_number} found at index {result2}.")
else:
    print(f"Recursive Binary Search: Seat {seat_number} not found.")
