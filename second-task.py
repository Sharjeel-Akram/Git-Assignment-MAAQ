def sub(num1 , num2):
	result = num1 - num2
	return result

def div(num1, num2):
	result = num1/num2
	return result

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))


if num1 > num2:
	result = div(num1, num2)
	print("Result of Division is: ", result)
else:
	result = sub(num1, num2)
	print("Result of Subtraction is: ", result)