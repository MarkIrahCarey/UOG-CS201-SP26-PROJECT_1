"""
Author: Mark Ira Galang
Date: 3/15/26
FileName: statistical_analyzer.py
Purpose: This program asks the user for a number of inputs (at least 3).
Then with those numbers calculates or gets the following
Max and Minimum Number
The sum and average
Total amount of numbers

The user also has the option to get a random number of inputs
Given the range and the amount of numbers
"""
# import modules
import random 

# greets the user!
print("""
Hello User! Welcome to the statistical analyzer.
This program simply asks at least 3 numbers from you and grabs the following: 
- The minimum and maximumimum number
- The sum and average
- And total of numbers given
      
You also have the option to randomly choose numbers within a range!
      """)

while True:
    # grab the user's choice
    choice = int(input("Would you like to choose your numbers or pick at random? \nEnter 1 for choosing, enter 2 for random: "))

    # make sure the user enteres the correct input
    while choice != 1 and choice != 2:
        choice = int(input("Invalid input, please try again: "))

    # set some variables that will constantly update
    maximum, minimum, sum, average, total_count = 0, 0, 0, 0, 0

    # create the code for choosing
    if (choice == 1):
        print("You have entered 1...")

        # create the loop
        while True:
            num = input("Enter a number or press enter to stop: ")

            # check if user wants to exit
            if num == "" and total_count >= 3:
                print("You have stopped... doing calculations")
                break
            elif num == "" and total_count < 3:
                print("You did not enter 3 numbers. You entered %d numbers" % (total_count - 1))
                continue # skip every code below this statement
            
            # start making calculations
            num = float(num)

            # first if this is the first iteration
            if total_count == 0:
                # we want to set the minimum and maximumimum as the first number
                minimum = num
                maximum = num

            # otherwise check for maximum
            if maximum < num:
                maximum = num
            
            # check for minimum 
            if minimum > num:
                minimum = num
            
            # add up the sum
            sum += num

            # incement the count
            total_count += 1

    # this else statement is for if they pick for random
    else:
        # ask for the following: total and range
        total_numbers = int(input("Please enter how many numbers you'd like (minimum 3): "))

        while total_numbers < 3:
            total_numbers = int(input("Invalid input. Please try again: "))
        
        min_range = int(input("Enter the minimum number: "))
        maximum_range = int(input("Enter the maximumimum number: "))

        while min_range > maximum_range:
            print("Your range is invalid, please try again: ")
            min_range = int(input("Enter the minimum number: "))
            maximum_range = int(input("Enter the maximumimum number: "))

        for i in range(total_numbers):
            # get a random number
            rand_num = random.randint(min_range, maximum_range)
            # print random number
            print("Random number %d: %d" % (total_count + 1, rand_num))


            # do the same calculations as above
            if total_count == 0:
                # we want to set the minimum and maximum as the first number
                minimum = rand_num
                maximum = rand_num

            # check for maximum
            if maximum < rand_num:
                maximum = rand_num
            
            # check for minimum
            if minimum > rand_num:
                minimum = rand_num
            
            # add up the sum
            sum += rand_num

            # incement the count
            total_count += 1

    # calculate the average
    average = sum / total_count

    # then at the end, print out the results
    print("="*20, "Results!", "="*20)
    print("Minimum number: %d" % minimum)
    print("Maximum number: %d" % maximum)
    print("Total Sum: %d" % sum)
    print("Average: %0.2f" % average)
    print("Total numbers: %d" % total_count)

    repeat = input("Would you like to do this again (y / n): ")

    while repeat != "y" and repeat != "n":
        repeat = input("Invalid input, please try again (y / n): ")
    
    if repeat == "n":
        print("Ending program... Thank you for using statistical analyzer :).")
    else:
        print("Alright!")
