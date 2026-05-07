food = ("idli","dosa","vada ")

for i in food :
    print(f"{i} is a south indian food")


stundents_marks = {"manoj": 25, "suresh": 30, "ramesh": 35}
for i , j in stundents_marks.items():
    print(f"{i}--> {j}")


stundents = ("manoj", "suresh", "ramesh")
marks = [25, 30, 35]
for i , j in zip(stundents, marks) :
    print(f"{i} --> {j}")
