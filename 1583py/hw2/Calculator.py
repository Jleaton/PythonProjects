import sys

inputChoice = 0;

while inputChoice != -1:
		
	inputChoice = int(input("\n To add enter 1\n to subtract enter 2\n to multiply enter 3\n to divided enter 4\n to quit enter -1\n "))
	

	if inputChoice == 1:
		
		firstNum = int(input("\nEnter first number: ")) 
		secondNum = int(input("Enter second number: "))

		sumResult = firstNum + secondNum
		print "\nThe sum is" , sumResult , "\n"
	
	if inputChoice == 2:
	
		firstNum = int(input("\nEnter first number: ")) 
		secondNum = int(input("Enter second number: "))

       		difference = firstNum - secondNum
		print "\nThe difference is" ,  difference , "\n"	
		
	if inputChoice == 3:

		firstNum = int(input("\nEnter first number: ")) 
		secondNum = int(input("Enter second number: "))

		product = firstNum * secondNum
		print "\nThe product is "  , product , "\n"

	if inputChoice == 4:

		firstNum = int(input("\nEnter first number: ")) 
		secondNum = int(input("Enter second number: "))

		dividend = firstNum / secondNum
		print "\nThe dividend is "  , dividend , "\n"

			
