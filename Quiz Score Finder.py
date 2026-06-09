scores = [85, 92, 78, 88, 90, 95, 80, 82, 91, 87]
n, target_score = len(scores), 88
print("Quiz Score Finder")
print("Quiz Scores:", scores , "target score:", target_score)
print()
steps = 0
for i in range(n):
    steps += 1
    if scores[i] == target_score:
        print(f"Score {target_score} found at index {i} in {steps} steps.")
        break
print()
lo , hi , steps = 0 , n-1 , 0
while lo<=hi:
    steps += 1
    mid = (lo + hi) // 2
    if scores[mid] == target_score:
        print(f"Score {target_score} found at index {mid} in {steps} steps.")
        break
    elif scores[mid] < target_score:
        lo = mid + 1
    else:
        hi = mid - 1
else:
    print(f"Score {target_score} not found in the list.")

def binary_search(scores, lo , hi , target_score , calls = 0):
    calls += 1
    if lo > hi:
        return -1 , calls
    mid = (lo + hi) // 2
    if scores[mid] == target_score:
        return mid , calls
    elif scores[mid] < target_score:
        return binary_search(scores, mid + 1, hi, target_score, calls)
    else:
        return binary_search(scores, lo, mid - 1, target_score, calls)
index, calls = binary_search(scores, 0, n - 1, target_score)
print(f"Recursive Binary Search: Score {target_score} found at index {index} in {calls} calls.")
print()
print("Space Complexity ")
print("Iterative Binary Search: O(1) - Only a few variables are used.")
print("Recursive Binary Search: O(log n) - Due to recursive call stack.")
print("Time Complexity ")
print("Iterative Binary Search: O(log n) - Each step halves the search space.")
print("Recursive Binary Search: O(log n) - Each call halves the search space.")