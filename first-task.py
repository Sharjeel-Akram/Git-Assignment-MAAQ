def add(num1, num2):
	sum = num1 + num2
	return sum

def mul(num1, num2):
	result = num1 * num2
	return result


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
	result = add(num1, num2)
	print("Result of addition is: ", result)
else:
	result = mul(num1, num2)
	print("Result of multiplication is: ", result)