#while loop
pin = "1234"
trials = 1

while trials <= 3 :
  
  input_pin = input(f"Trials- {trials} | PIN >>")
  trials += 1


  if input_pin == pin :
    print("CORRECT , WELCOME BACK HERO ")
    break 
  else :
    print("INCORRECT , TRY AGAIN")