'''st=input("enter string:")
try:
    int1=int(st)
    print("converted string",int1)
except ValueError:
    print("Enter a valid string")'''

'''d1 = int(input("enter the dividened"))
d2=int(input("enter divisor"))
try:
    q1=d1/d2
    print("Quotient:",q1)
except ZeroDivisionError:
    print("Cannot divide by zero")'''

'''lst=[1,2,3,4,5,6,7]
try:
    n=int(input("enter index:"))
    print("lst element:",lst[n])
except IndexError:
    print("enter a valid index")
    '''

'''
n=input("enter file name:")
try:
    with open("data.txt","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found")
'''
'''
print("\n5.Login System with custom exception")
username="admin"
password="1234"
attempts =3
while attempts>0:
    usernamee=input("enter user name:")
    passwordd=input("enter password:")
    if usernamee==username and passwordd==password:
        print("login successfull")
        break
    else:
        attempts -=1
        print("Wong info")
        print("Attempts left:",attempts)
        
'''
'''
B=input("enter string")
try:
    f1=float(B)
    print("Converted float:",f1)
except ValueError:
    print("Enter a valid string")'''
'''
BAL = int(input("Enter balance: "))
Am = int(input("Enter amount to be withdrawn: "))
try:
    if Am > BAL:
        raise ValueError("Insufficient Balance")
    BAL -= Am
    print("Amount withdrawn:", Am)
    print("Remaining balance:", BAL)
except ValueError as e:
    print(e)
'''
'''
class AgeError(Exception):
pass

try:
age = int(input("Enter age: "))

if age < 18:
raise AgeError("Not Eligible")

print("Eligible")

except ValueError:
print("Invalid Input")

except AgeError as e:
print(e)
'''
'''
try:
num1 = int(input("Enter number: "))
num2 = int(input("Enter second number: "))

result = num1 / num2

list1 = [1, 2, 3]

index = int(input("Enter index: "))

print(list1[index])

except ValueError:
print("Invalid Input")

except ZeroDivisionError:
print("Cannot divide by zero")

except IndexError:
print("Index out of range")

try:
file = open("hi.txt", "r")

print(file.read())

except FileNotFoundError:
print("File not found")

finally:
print("File Closed")
'''
