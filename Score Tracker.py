names = ["Jasraj" , "Divanshi" , "Satyarth" , "Shivansh" , "Aarav" ]
scores = [2, 3 , 4, 5, 6]
n = len(scores)
print("Score Tracker")
for i in range(n):
    print(i+1, "." , names[i] , ":" , scores[i] , "points")
print()
steps = 1
print("Score at Index 0 " , scores[0] , "steps" , steps)
print()
target = "Jasraj"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break
print(f"Score at Index {steps-1} " , scores[steps-1] , "steps" , steps)
print()
steps = 0
target_sum = 10
current_sum = 0
print("Finding the first index where the cumulative score exceeds 10...")
for i in range(n):
    for j in range(i + 1 , n ):
        steps += 1
        if scores[i] + scores[j] == target_sum:
            print(f"Score at Index {i} and {j} " , scores[i] , "+" , scores[j] , "=" , scores[i] + scores[j] , "steps" , steps)
            break
print(steps)
print()
