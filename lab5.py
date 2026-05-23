def sort_marks():

    marks = []

    print("Enter 6 subject marks:")

    for i in range(6):
        m = int(input())
        marks.append(m)

    for i in range(len(marks)):
        for j in range(0, len(marks)-i-1):

            if marks[j] < marks[j+1]:

                temp = marks[j]
                marks[j] = marks[j+1]
                marks[j+1] = temp

    print("marks from highest to lowest :")

    for m in marks:
        print(m)

sort_marks()