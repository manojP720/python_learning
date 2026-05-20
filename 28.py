num1 = float(input("enter frist num"))
num2 = float(input("enter second num"))

  print("choose operation")
  print("1-add")
  print("2-subtract")
  print("3-multi")
  print("4-div")

  choice = int(input(enter u r choice (1-4):))
  if choice == 1:
   print("Result=", num1 + num2 )
  elif choice == 2:
   print("Result=", num1 - num2 )
  elif choice == 3:
   print("Result=",num1 *num2)
  elif choice == 4:
   print("Result=",num1 / num2 )

  else:
    print("invaild")  