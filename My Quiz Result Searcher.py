scores = [85, 92, 78, 92, 88, 75, 85]
print("Quiz Result Searcher")
print("Scores:", scores)
index = int(input("Enter index to access score: "))
if 0 <= index < len(scores):
    print("Score at index", index, "=", scores[index])
else:
    print("Invalid index")
target = int(input("Enter score to search: "))
found = False
for i in range(len(scores)):
    if scores[i] == target:
        print("Score found at position", i)
        found = True
if not found:
    print("Score not found")
print("\nMatching Score Pairs:")
for i in range(len(scores)):
    for j in range(i + 1, len(scores)):
        if scores[i] == scores[j]:
            print(scores[i], "found at positions", i, "and", j)