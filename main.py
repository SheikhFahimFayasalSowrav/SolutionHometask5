# Question 1:
#  Make a code that will take the input of two strings. If the two inputs are the same, your program will print “SAME”.
#  ...If Not, It should show “NOT Same” and check which one is greater and print that.

# Answer to the Question No. 1:
print("\nAnswer to the Question No. 1\n")

Input1 = input('Please enter the 1st input: ')
Input2 = input('Please enter the 2nd input: ')

if Input1 == Input2:
    print("SAME")
else:
    print("NOT Same")
    if Input1 > Input2:
        print(Input1, 'is greater.')
    else:
        print(Input2, 'is greater.')


# Question 2
# Make a calculator, which will work as the following algorithm:
# a. Input 1st Number
# b. Input what you want to do with numbers (+, -, *, or /)
# c. Input 2nd Number
# d. Do calculation
# e. Show Result

# Answer to the Question No. 2:
print("\nAnswer to the Question No. 2\n")

# Making a calculator
print("Making a calculator\n")

input1 = float(input('Input 1st Number: '))
operator = input('Input what you want to do with the numbers (+, -, *, or /): ')
input2 = float(input('Input 2nd Number: '))

if operator == '+':
    addition = input1 + input2
    print(input1, '+', input2, '=', addition)

elif operator == '-':
    subtraction = input1 - input2
    print(input1, '-', input2, '=', subtraction)

elif operator == '*':
    multiplication = input1 * input2
    print(input1, '*', input2, '=', multiplication)

elif operator == '/':

    if input2 == 0:
        print('\'ZeroDivisionError\' occurred! Numbers cannot be divided by 0.')
    else:
        division = input1 / input2
        print(input1, '/', input2, '=', division)

else:
    print('Please provide a valid operator (+, -, *, or /) and run the program again.')


# Question 3
# Rainfall = [22, 3.4, 1, 8, 19, 21]
# From the above rainfall data, Find the average rainfall of that area.

# Answer to the Question No. 3:
print("\nAnswer to the Question No. 3\n")

# Average rainfall (without using formula)
print("Average rainfall (without using formula)")

Rainfall = [22, 3.4, 1, 8, 19, 21]

sum_elements = Rainfall[0] + Rainfall[1] #(22 + 3.4 + 1 + 8 + 19 + 21)
num_elements = 6
average_rainfall = sum_elements / num_elements

print('Average rainfall: ', average_rainfall)

# Question 4
# A school has the following rules for the grading system:
#   a. Below 25 - F
#   b. 25 to 45 - E
#   c. 45 to 50 - D
#   d. 50 to 60 - C
#   e. 60 to 80 - B
#   f. Above 80 – A
# Ask the user to enter marks and print the corresponding grade.

# Answer to the Question No. 4:
print("\nAnswer to the Question No. 4\n")

# Schools grading system
print("School's grading system\n")

mark = float(input('Enter the marks: '))

if mark < 25:
    print('The corresponding grade is: F')

elif (45 > mark >= 25):
    print('The corresponding grade is: E')

elif (mark >= 45) and (mark < 50):
    print('The corresponding grade is: D')

elif (mark >= 50) and (mark < 60):
    print('The corresponding grade is: C')

elif (mark >= 60) and (mark < 80):
    print('The corresponding grade is: B')

elif (mark >= 80) and (mark <= 100):
    print('The corresponding grade is: A')

else:
    print('Please enter the correct marks.')