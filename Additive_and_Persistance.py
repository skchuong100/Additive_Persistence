#Create a while loop so that the program will lopp infinitely unless a negative number is inputted
while(True):
  #Ask the user to input an integer
  user_num=int(input('Please enter an integer (negative integer to quit): '))
  print()
  #Declare variables in the beginning for different calculations to use so that the variables will avoid being assigned different numbers as the program calculates
  multi_num=user_num
  message_num=user_num
  add_persist=0
  total_sum=0
  multi_persist=0
  total_product=1
 
 #Create an if statement if the user inputs a negative number to end the program
  if user_num<0:
    print("Thank for playing with numbers...Goodbye")
    print()
    print("Process exit code 0")
    #Put a break here so that the program will stop if the user inputs a negative number
    break

  #Create an elif statement if the user inputs a single-digit integer
  elif 1<=user_num<=9:
    print("               Additive Persistence: 0, Additive Root: ", user_num)
    
  #Create an elif statement if the user inputs an integer that has two or more digits
  elif user_num>9:
    add_persist=0
    #Create a while loop so that it loops until the number is a single digit
    while user_num>9:
      #Create an accumulator to count how many times the sum of the digits is calculated
      add_persist+=1
      total_sum=0
      #Create a while loop so that it stops when it goes below 0
      while user_num>0:
        #By using the remainder function, the input can be split one number at a time
        split_num=user_num%10
        #This will be use to accumulate the sum with the addition of numbers that are split off from the input
        total_sum+=split_num
        user_num//=10   
      user_num=total_sum
    print('For the integer:', message_num)
    print("               Additive Persistence: ", add_persist,', Additive Root: ', total_sum, sep='')
  
  #Create an if-else statement to do calculations for multiplicative persistence and root
  #Create an if statement if the user inputs a single digit
  if multi_num<9:
    print('               Multiplicative Persistense: 0, Multiplicative Root: ', multi_num)
    
  else:
    multi_persist=0
    #Create a while loop so that it continues until the input is less than one digit
    while multi_num>9:
      multi_persist+=1
      total_product=1
      while multi_num>0:
        #Use the remainder function to split what the user inputted one by one
        split_num=multi_num%10
        #Create an accumulator to multiply the splitted numbers together
        total_product=total_product*split_num
        multi_num=multi_num//10
      multi_num=total_product

    print('               Multiplicative Persistense: ', multi_persist,', Multiplicative Root: ', total_product, sep='')
