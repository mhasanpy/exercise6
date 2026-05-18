# 1. Print numbers from 1 to 20 using while loop
# 2. Print numbers from 1 to 20 using for loop
# 3. Print all even numbers between 1 to 50
# 4. Print all odd numbers between 1 to 50
# 5. Print numbers from 30 to 1 in reverse order
# 6. Print your name 10 times using loop
# 7. Print all numbers divisible by 3 from 1 to 100
# 8. Print all numbers divisible by 5 and 7 from 1 to 100
# 9. Find the sum of numbers from 1 to 50
# 10. Find the sum of even numbers from 1 to 100

# 11. Multiplication table of 7
# 12. Multiplication table of any number (take input from user)
# 13. Count how many even numbers are there between 1 and 200
# 14. Count how many odd numbers are there between 1 and 200
# 15. Find factorial of a number (using loop)
# 16. Reverse a given number (e.g., 12345 → 54321)
# 17. Find sum of digits of a number (e.g., 1234 = 1+2+3+4 = 10)
# 18. Count total number of digits in a number
# 19. Print square of numbers from 1 to 15
# 20. Print cube of numbers from 1 to 12

# 21. Check whether a number is positive, negative or zero
# 22. Check if a number is even or odd
# 23. Find the largest number among three numbers
# 24. Check if a year is leap year or not
# 25. Print all vowels from a given string
# 26. Count vowels and consonants in a string
# 27. Print characters of a string one by one using loop
# 28. Reverse a string using loop (without using slicing)
# 29. Find the largest number from a list of 10 numbers
# 30. Find the smallest number from a list of 10 numbers

# 31. Print this pattern:
# *
# **
# *
# **
# ***

# 32. Print this pattern:
# ***
# **
# *
# **
# *

# 33. Print this pattern:
# 1
# 12
# 123
# 1234
# 12345

# 34. Print this pattern:
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# 35. Create a list of 10 numbers and print sum and average of all numbers
# 36. Count how many numbers are greater than 50 in a list
# 37. Take 5 student names and their marks, then print average marks
# 38. Create a dictionary of 5 students (name: marks) and print all names and marks
# 39. Take a sentence and count how many words are there
# 40. Take a list of numbers and create two new lists: one for even numbers and one for odd numbers

# 1. Print numbers from 1 to 20 using while loop
print("-----------------------------------Print numbers from 1 to 20 using while loop--------------------------")
number = 1
while number <= 20:
    print(number)
    number += 1

print("-----------------------------------Print numbers txt from  using while loop--------------------------")
number = 1
while number <= 20:
    print(number, end=" ")
    number += 1
    numbers  ={"0"}
    print(" numbers ")

print("one line  from 2 add  using while loop ----")
number = 2
while number <= 20:
    print(number)
    number += 2




# 2. Print numbers from 1 to 20 using for loop
print("-------------------Print numbers from 1 to 20 using ____________for___________ loop-------------------")

# basic 
print("basic for using")
for number in range(0, 23):
    print(number)


# All numbers on one line
print("all numbers in one line")
for number in range(1, 29):
    print(number, end=" ")

# Even numbers only
print("Even numbers only")
for number in range(2, 21, 2):
    print(number)



    # Odd numbers only
print(" Odd numbers only")
for number in range(1, 21, 2):
    print(number)



# Reverse order
print(" Revers order")
print(" Reverse order ")
for number in range(20, 0, -1):
    print(number)



#With custom text
print("------------------ print with custom text")
for number in range(11, 21):
    print(f"Current number is {number}")


#With squares
print("-----------------------for loop  with squares and cube ")
for number in range(1, 9):
    print(f"{number} squared = {number**3}")

    print(f"{number} cube = {number**3}")



    #Store in a list
print("-----------------------------------Store in a list------------")
numbers = [number for number in range(1, 21)]
print(numbers)



#Skip numbers (step size)
print("-------------------------Skip numbers (step size)--------------------------")
print("skip numbers (step size")
for number in range(1, 23, + 3):
    print(number)

for number in range(- 1, - 22, -3):
    print(number)


# Multiplication table (nested loop)
print("--------------Multiplication table ( nested loop)------")
for number in range(0, 11):
    print(f"Table of {number}:")


print("----------------Multiplier number------------------")
for multiplier in range(0, 6):
    print(f"{number} x {multiplier} = {number * multiplier}")
    print("-" * 20)


## 3. Print all even numbers between 1 to 50
print("-----------------------------print all even numbers between 1 to 50 ----------------")

#Triangle pattern of even numbers
print("Triangle pattern of even numbers")
for i in range(2, 31, 2):
    for j in range(2, i+1, 2):
        print(j, end=" ")
    print()





print("-----------Triangle pattern of even subtraction (-) numbers")

for i in range(1, 22,2):
    for j in range(1, i-2, 3):
        print(j, end=" ")
    print()


print("-------------------Triangle pattern of even Asterisk [Multication] (*) numbers" )

for i in range(1, 9,2):
    for j in range(1, i*5,  3):
        print(j, end=" ")
    print("-" * 2)


    print("-------------------Triangle pattern of  even Forward Slash] Divition (/) numbers" )

for i in range(1, 9,2):
    for j in range(1, i+5,  3):
        print(j, end=" / ")
    print()
    


#Pyramid pattern
print("-------------------- pattern of even Pyramid pattern_________")
for i in range(2, 51, 2):
    spaces = " " * (50 - i)
    numbers = " ".join(str(j) for j in range(2, i+1, 2))
    print(spaces + numbers)
print()


#Reverse triangle
print("---------------Reverse triangle---------------")
for i in range(50, 1, -2):
    for j in range(2, i+1, 2):
        print(j, end=" ")
print()


#Checkerboard style (rows of even numbers)
print("------------------Checkerboard style (rows of even numbers)---------")
for row in range(1, 6):
    for col in range(2, 51, 2):
        print(col, end=" ")
print()


#Even number multiplication table
print("--------------------Even number multiplication table-----------")
for number in range(2, 23, 2):
    print(f"Table of {number}:")
    for multiplier in range(1, 6):
        print(f"{number} x {multiplier} = {number * multiplier}")
print("-" * 20)



## 4. Print all odd numbers between 1 to 50
print("---------------------4 -___Print all odd numbers between-------------")


#Odd numbers only
("--------------------5 Odd numbers only-------------")
for number in range(1, 13, 2):
    print(number)

#Using condition inside loop
print("--------------------------Using condition inside loop----------")
for number in range(1, 11):
    if number % 2 != 0:
        print(number)

#Store odd numbers in a list
# print("----------------------------Store odd numbers in a list---------------")
odd_numbers = [number for number in range(1, 15) if number % 2 != 0]
print(odd_numbers)





#Multiplication table for odd numbers
print("--------------------------------Multiplication table for odd numbers-----------")
for number in range(1, 21, 2):
    print(f"Table of {number}:")
    for multiplier in range(1, 6):
        print(f"{number} x {multiplier} = {number * multiplier}")
    print("-" * 20)

    ## # Print numbers from 30 to 1 in reverse order
print("----------6 Print numbers from 30 to 1 in reverse order--------------")

for i in range(30, 0, -1):
    print(i)



## 6. Print your name 10 times using loop
print("-------------------------Print your name 10 times using loop-----------")

# Print your name 10 times
for i in range(10):
    x = "What is Your Name?"
    print(x + " _Mehedi Hasan_")


## 6. Print your name is one line  15 times using loop
print("-------------------------------------------6 Print your name is one line  15 times using loop------------")

for i in range(15):
    print("My name ,", end=" ")





## 7. Print all numbers divisible by 3 from 1 to 100
print("----------------------------------------------------------7. Print all numbers divisible( % ) by 3 from 1 to 100-------------------------------------------------------------oooooooooo")
for i in range(1, 101):
    if i % 3 == 0:
        print(i, end=" ")


print("----------------------------------------------------------7. Print all numbers divisible( % ) by 3 from 1 to 100------one line-------------------------------------------------------oooooooooo")
for i in range(3, 101, 3):
    print(i)


## 8. Print all numbers divisible by 5 and 7 from 1 to 100
print("-------------------------------# 8. Print all numbers divisible by 5 and 7 from 1 to 100-----------------------")
# Print numbers divisible by both 5 and 7 from 1 to 100
for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i)

print("-------------------------------# 8. Print all numbers in ______one line__________ divisible by 5 and 7 from 1 to 100-----------------------")
for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=" ")



## 9. Find the sum of numbers from 1 to 50
print("-----------------------# 9. Find the sum of numbers from 1 to 50--------------")
# Find the sum of numbers from 1 to 50
total = 0
for i in range(1, 51):
    total += i
print("The sum is:", total)


print("The sum is:", sum(range(1, 51)))


## 10. Find the sum of even numbers from 1 to 100
print("-----------------------# 10. Find the sum of even numbers from 1 to 100---------------------")
# Find the sum of even numbers from 1 to 100
total = 0
for i in range(2, 101, 2):  # start at 2, step by 2
    total += i
    
print("The sum of even numbers from 1 to 100 is:", total)



# 11. Multiplication table of 7
print("-------------------# 11. Multiplication table of 7------------------------")


# Multiplication table of 7
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")


#Using a Function
print("Using a Function")

def multiplication_table(number, upto=10):
    for i in range(1, upto + 1):
        print(f"{number} x {i} = {number * i}")

# Call the function
multiplication_table(7)



##With User Input
print("------# 12. Multiplication table of any number (take input from user)----------")

def multiplication_table(number, upto=10):
    print(f"\nMultiplication Table of {number}\n")
    for i in range(1, upto + 1):
        print(f"{number} x {i} = {number * i}")

# Get user input
num = int(input("Enter the number: "))
upto = int(input("Enter the range: "))
# Call the function
multiplication_table(num, upto)



print("-------With User Input-- # Ask user for a number--")
# Ask user for a number
num = int(input("Enter a number: "))
upto = int(input("Enter the range: "))

for i in range(1, upto + 1):
    print(f"{num} x {i} = {num * i}")


## 13. Count how many even numbers are there between 1 and 200
print("--------------# 13. Count how many even numbers are there between 1 and 200---------------")

count = 30
for i in range(1, 201):
    if i % 2 == 0:
     count += 1
print("Total even numbers between 1 and 200:", count)

#Using List Comprehension
print("-------------------Using List Comprehension--------------")

# List comprehension method
count = len([i for i in range(1, 201) if i % 2 == 50])
print("Total even numbers between 1 and 200:", count)


#Shorter Version with
print("---------------------Shorter Version with------------------------")
# Using range step
even_numbers = list(range(2, 201, 2))
print("Total even numbers between 1 and 200:", len(even_numbers))

# 14. Count how many odd numbers are there between 1 and 200
print("---------------------# 14. Count how many odd numbers are there between 1 and 200-------------")

# Count odd numbers between 1 and 200

count = 0
for i in range(1, 201):
    if i % 2 != 0:
        count += 1

print("Total odd numbers between 1 and 200:", count)


#Shorter Version with range()
print("--------------Shorter Version with range()------------------")
# Using range step
odd_numbers = list(range(1, 100, 2))
print("Total odd numbers between 1 and 200:", len(odd_numbers))

# 15. Find factorial of a number (using loop)
print("--------------find factorial of a number (using loop-------------------")
# Factorial using loop

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")


# 16. Reverse a given number (e.g., 12345 → 54321)
print("------------------------# 16. Reverse a given number (e.g., 12345 → 54321)-----------------")
# Reverse a number using loop

num = int(input("Enter a number: "))
reverse_num = 0

while num > 0:
    digit = num % 10          # extract last digit
    reverse_num = reverse_num * 10 + digit
    num = num // 10           # remove last digit

print(f"Reversed number is {reverse_num}")


## 17. Find sum of digits of a number (e.g., 1234 = 1+2+3+4 = 10)
print("------------------# 17. Find sum of digits of a number (e.g., 1234 = 1+2+3+4 = 10)--------------")
# Sum of digits of a number

num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    digit = num % 10         # extract last digit
    sum_digits += digit      # add digit to sum
    num = num // 10          # remove last digit

print(f"Sum of digits is {sum_digits}")




## 18. Count total number of digits in a number
print("----------------# 18. Count total number of digits in a number----------")
# Count total number of digits in a number

# Input number from user
num = int(input("Enter a number: "))

# Initialize counter
count = 0

# Loop until number becomes 0
while num != 0:
    num //= 10   # Remove last digit
    count += 1   # Increase digit count

# Print result
print("Total number of digits:", count)



# 19. Print square of numbers from 1 to 15
print("-----------squares of numbers from 1 to 15--------")
for i in range(1, 16):
    print(f"The square of {i} is {i*i}")


## 20. Print cube of numbers from 1 to 12
print("---------# 20. Print cube of numbers from 1 to 12--------")
# Print cubes of numbers from 1 to 12

for i in range(1, 13):
    print(f"The cube of {i} is {i**3}")


## 21. Check whether a number is positive, negative or zero
print("-------------------------# 21. Check whether a number is positive, negative or zero-----------------")
# Check whether a number is positive, negative or zero

num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")



## 22. Check if a number is even or odd
print("---------------## 22. Check if a number is even or odd-----------")
# Check if a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")



# 23. Find the largest number among three numbers
print("=------------------------# 23. Find the largest number among three numbers------------")
# Find the largest number among three numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")

##24. Check if a year is leap year or not
print("__________-# 24. Check if a year is leap year or not-----_____________")
# Check if a year is leap year or not

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")


##25. Print all vowels from a given string
print("-----------------# 25. Print all vowels from a given string--------")
# Print all vowels from a given string

text = input("Enter a string: ")
vowels = "aeiouAEIOU"

print("Vowels in the string are:")
for char in text:
    if char in vowels:
        print(char, end=" ")






# 26. Count vowels and consonants in a string
print("----------------# 26. Count vowels and consonants in a string------------")
# Count vowels and consonants in a string

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():  # check if character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")





# 27. Print characters of a string one by one using loop
print("# 27. Print characters of a string one by one using loop-----------------")
# Print characters of a string one by one

text = input("Enter a string: ")

print("Characters in the string are:")
for char in text:
    print(char)





# 28. Reverse a string using loop (without using slicing)
print("--------------# 28. Reverse a string using loop (without using slicing)---------")


# Input string
text = input("Enter a string: ")

# Initialize an empty string to store the reversed result
reversed_text = ""

# Loop through the string in reverse order
for char in text:
    reversed_text = char + reversed_text

# Print the reversed string
print("Reversed string:", reversed_text)



# 29. Find the largest number from a list of 10 numbers
print("--------------------------# 29. Find the largest number from a list of 10 numbers-----------")

# Input: 10 numbers from the user
numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Initialize largest with the first number
largest = numbers[0]

# Loop through the list to find the largest
for num in numbers:
    if num > largest:
        largest = num

# Print the largest number
print("The largest number is:", largest)



# 30. Find the smallest number from a list of 10 numbers
print("---------------# 30. Find the smallest number from a list of 10 numbers-------------")


# Input: 10 numbers from the user
numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Initialize smallest with the first number
smallest = numbers[0]

# Loop through the list to find the smallest
for num in numbers:
    if num < smallest:
        smallest = num

# Print the smallest number
print("The smallest number is:", smallest)



##31. Print this pattern:
# *
# **
# *
# **
# ***
print("# 31. Print this pattern *********")
# Print the pattern:
# *
# **
# *
# **
# ***

# Using print statements directly
print("*")
print("**")
print("*")
print("**")
print("***")


print("*")
print("**")
print("***")
print("****")
print("******")
print("**********")
print("*************")


# Alternative: Using a loop
print("---------# Alternative: Using a loop-------------")
pattern = ["*", "**", "*", "**", "***"]

for line in pattern:
    print(line)



# Print the pattern:
# 1
# 12
# 123
# 1234
# 12345
print(" Print the pattern:1, 12, 123, 1234, 12345 ,Using nested loops ")
 #Using nested loops
for i in range(1, 6):          # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for numbers in each row
        print(j, end="")       # Print numbers on the same line
    print()                    # Move to the next line


# 34. Print this pattern:
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

print("--------------# 34. Print this pattern:5 5 5 5 5,4 4 4 4,3 3 3,2 2,1")
# Print the pattern:
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# Using nested loops
for i in range(5, 0, -1):          # Outer loop goes from 5 down to 1
    for j in range(i):             # Inner loop prints the number 'i' multiple times
        print(i, end=" ")          # Print the number with a space
    print()                        # Move to the next line

# 35. Create a list of 10 numbers and print sum and average of all numbers
print("-----------------# 35. Create a list of 10 numbers and print sum and average of all numbers-----------")


# Input: 10 numbers from the user
numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate sum
total = 0
for num in numbers:
    total += num

# Calculate average
average = total / len(numbers)

# Print results
print("Numbers entered:", numbers)
print("Sum of numbers:", total)
print("Average of numbers:", average)


# 36. Count how many numbers are greater than 50 in a list
print("--------------------------------# 36. Count how many numbers are greater than 50 in a list--------")
# Count how many numbers are greater than 50 in a list

# Input: 10 numbers from the user
numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Count numbers greater than 50
count = 0
for num in numbers:
    if num > 50:
        count += 1

# Print results
print("Numbers entered:", numbers)
print("Count of numbers greater than 50:", count)


# 37. Take 5 student names and their marks, then print average marks
print("-----------# 37. Take 5 student names and their marks, then print average marks---------")
# Take 5 student names and their marks, then print average marks

students = []
marks = []

# Input: 5 student names and marks
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    mark = float(input(f"Enter marks of {name}: "))
    students.append(name)
    marks.append(mark)

# Calculate average marks
total = 0
for m in marks:
    total += m

average = total / len(marks)

# Print results
print("\nStudent Marks:")
for i in range(5):
    print(f"{students[i]}: {marks[i]}")

print("\nAverage Marks:", average)



# 38. Create a dictionary of 5 students (name: marks) and print all names and marks
print("----# 38. Create a dictionary of 5 students (name: marks) and print all names and marks-------")
# Create a dictionary of 5 students (name: marks) and print all names and marks

# Input: 5 student names and marks
students = {}

for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    mark = float(input(f"Enter marks of {name}: "))
    students[name] = mark

# Print all names and marks
print("\nStudent Marks:")
for name, mark in students.items():
    print(f"{name}: {mark}")


# 39. Take a sentence and count how many words are there
print("-----------# 39. Take a sentence and count how many words are there---------")
# Take a sentence and count how many words are there

# Input sentence from user
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Count words
count = len(words)

# Print results
print("Sentence entered:", sentence)
print("Number of words:", count)


# 40. Take a list of numbers and create two new lists: one for even numbers and one for odd numbers
print("------------# 40. Take a list of numbers and create two new lists: one for even numbers and one for odd numbers--------")
# Take a list of numbers and create two new lists: one for even numbers and one for odd numbers

# Input: numbers from the user
numbers = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Separate even and odd numbers
even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Print results
print("\nNumbers entered:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)


