scores = [90 , 72 , 85 , 70 , 88 , 97]

print("\n ================= Part 1 : Head and Tail ================== \n")

def head_tail(lst):
    if len(lst) == 0:
        print("Reached Empty List")
        return
    print("Head (lst[0])    :", lst[0])
    print("Tail (lst[1:])   :", lst[1:])
    print()
    head_tail(lst[1:])
head_tail(scores)

print("\n ================= Part 2 : Base Case Trace ================== \n")

def trace_base(lst):
    print("Current List -->" , lst)
    if len(lst) == 0:
        print("Base Case Reached") # Removed lst[0] as the list is empty
        return
    trace_base(lst[1:])
trace_base(scores)

print("\n ================= Part 3 : Sorted Check ================== \n")

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

print("\n ================= Part 4 : Sum Of Scores ================== \n")

def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + recursive_sum(lst[1:])
total = recursive_sum(scores)
print("Total Score of the list is :", recursive_sum(scores))    

print("\n ================= Part 5 : Champion Score ================== \n")

def highest_score(lst):
    if len(lst) == 1:
        return lst[0]
    highest = highest_score(lst[1:])
    if lst[0] > highest:
        return lst[0]
    else:
        return highest
champion_score = highest_score(scores)
print("Champion Score of the list is :", champion_score)

print("\n ================= Program Completed ================== \n")