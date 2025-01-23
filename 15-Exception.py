while True:               
    try:
        User_input = int(input('Enter a number: '))   
              
    except ValueError:
        print("The input you've provided is not value")     ### Here we did not use any break statment so it works under infinite while loop

       
print(f'User input is {User_input}')  ### it never print as the above code is under infinte while loop