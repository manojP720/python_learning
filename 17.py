#while loop
pin = "1234"

while True :
  
  input_pin = input("PIN >>")


  if input_pin == pin :
    print("CORRECT , WELCOME BACK HERO ")
    break 
  else :
    print("INCORRECT , TRY AGAIN")