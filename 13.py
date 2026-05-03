#develop a program to sort the

lines = ["dog", "cat", "apple", "banana", "grape"]
sorted_lines =  []

for line in lines :
    sorted_lines.append(line.strip())
sorted_lines.sort()

f2 =  open("output.txt","w")
for line in sorted_lines:
    f2.write(line + "\n")

x = f2.close()
print(" The contents sorted and written to output.txt")