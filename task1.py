# Syntax of python
print("Hello World")

print('\n') #new line

# Variables in Python
x = 40                      # x is of type int
x = "Bangladesh"            # x is now of type str
print(x)
print(type(x))
print('\n') #new line

# Print Function
print('"Welcome to Python!')

print('Welcome','to','phthon!')  # Printing a Comma-Separated List of Items

print("Welcome\nto\n\nPython!")   # Printing Many Lines of Text with One Statement
print('\n') #new line


# Arithmetic operators

a = 60
b = 15
add = a + b 
sub = a - b 
mul = a * b 
mod = a % b 
p = a ** b 
print(add) 
print(sub) 
print(mul) 
print(mod) 
print(p) 

print('\n')  #new line

#Relational & Assignment Operators

a = 20
b = a 
print(b) 
b += a 
print(b) 
b -= a 
print(b) 
b *= a 
print(b) 
b <<= a 
print(b)

print('\n') #new line

#Boolean Type

a = True
b = False
print(a and b) 
print(a or b) 
print(not a) 


print('\n') 


#Printing Expression with Escape Sequences
print('Sum is', 7 + 3)
print('\n') #new line

#Getting Input from the User
name = input("What's your name? ")
print(name)
print('\n') #new line

#Multiple Input from the User
print('output of Multiple input from user:')
print('Enter Two numbers: ')
a, b = input().split()
print('Output: ', a , ' ' , b)
print('sum: ', int(a) + int(b))

print('\n') #new line

# Conditional statement

#if else
print('Enter Your Two Numbers: ')
a, b = input().split()
if a>b:
    print(a, 'is bigger than',b)
elif a<b:
    print(a,'is less than',b)  
else:
    print(a,'is equals to',b) 

print('\n')

# while loop
print('Enter a number: ')
a = input()
a = int(a)
x = 1
print('numbers from 1 to ', a , 'are: ')
while x <= a:
    print(x, end=' ')
    x = x + 1

print('\n')  

# break in while loop


# Using 'break' in a loop
print('Output of break inside the loop:')
friends = ["Rasel", "Junayed", "Tamim", "Shakib", "Rakib", "Samiya", "Hamim"]
for friend in friends:
    print(friend, end=' ')
    if friend == "Rakib":
        break  # Stops the loop when "Rakib" is encountered

print('\n')


#continue in loop

friends = ["Rasel", "Junayed", "Tamim", "Shakib", "Rakib"]
for friend in friends:
    if friend == "Tamim":
        continue  # Skips the rest of the code in this iteration when "Tamim" is encountered
        print(friend, end=' ')

print('\n')

#For Loop
for i in range(0, 10, 2): 
    print(i) 
print('\n')   

#Range Function 
#Create a sequence of numbers from 3 to 5, and print each item in the sequence
x = range(3, 6)
for n in x:
  print(n)
print('\n')  
for i in range(5):
    print(i, end=" ")
print()

print('\n')



print('Numbers from 20 to 50')
for x in range(20 , 50):
    q = q + x
    print(x, end=' ')
print('Sum: ', q)
    
print('\n')    

print('Even Numbers from 20 to 50')
for x in range(20 , 50, 2):
    q = q + x
    print(x, end=' ')
print('Sum: ', q)
    



print('Numbers from 100 to 50')
for x in range(100 , 50, -2):
    q = q + x
    print(x, end=' ')
print('Sum: ', q)
    
print('\n') 
 




