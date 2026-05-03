#develop a program to sort the
f1 = open("input.txt","r")
lines = f1.readlines()
sorted_lines =  []

for line in lines :
    sorted_lines.append(line.strip())
sorted_lines.sort()

f2 =  open("output.txt","w")
for line in sorted_lines:
    f2.write(line + "\n")

f1.close()
f2.close()  
print(" The contents sorted and written to output.txt")