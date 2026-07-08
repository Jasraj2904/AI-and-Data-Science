scores = [90 , 95 , 88 , 70 , 83 , 76]

print("\n ================= Leaderboard Analyzer ================= \n")

print("\n ================= Part1 : Head and Tail ================== \n")

def print_head_tail(lst):
    if len (lst) == 0:
        print("Reached Empty List")
        return
    print("Head (lst[0])    :", lst[0])
    print("Tail (lst[1:])   :", lst[1:])
    print_head_tail(lst[1:])
print_head_tail(scores)

print("\n ================= Part2 : Base Case Trace ================== \n")

def trace_base(lst):
    print("Current List -->", lst)
    if len(lst) == 0:
        print("Base Case Reached") # Removed lst[0] as the list is empty
        return
    trace_base(lst[1:])
trace_base(scores)

print("\n ================= Part3 : Sorted Check ================== \n")

def is_sorted(lst):
    if len(lst) <= 1:
        return True
    if lst[0] < lst[1]:
        return False
    return is_sorted(lst[1:])
if is_sorted(scores):
    print("The list is sorted in descending order")
else:
    print("The list is not sorted in descending order")

print("\n ================= Part4 : Sum Of Scores ================== \n")

def total_score(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + total_score(lst[1:])
print("Total Score of the list is :", total_score(scores))

print("\n ================= Part5 : Champion Score ================== \n")

def champion(lst):
    if len(lst) == 1:
        return lst[0]
    best = champion(lst[1:])
    if lst[0] > best:
        return lst[0]
    else:
        return best
    
print("Champion Score of the list is :", champion(scores))

print("\n ================= Program Completed ================== \n")