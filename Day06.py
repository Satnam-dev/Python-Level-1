# Exceptional Handling (Used to handle error in program)
# Prevent program from crashing
# improbe reliability(able to work correctly)
# try,except
# Types of error
# 1.Value Error
# 2.ZerDivisionError
# 3.SystemError
# 4.KeyError
# 5.InterruptedError
# 6.IndexError
# 7.TypeError
# 8.FileNotFoundError
# 9.identtialError

try:
    number=int(input("Enter your number-")) # Run zero it will not run to solve it we use try.
    result=40/number
    print("Your result is ",result)
except ZeroDivisionError:
    print("Error Occurred")
except ValueError:
    print("Error Occurred")
finally:
    print("Program Executed")

# You are printing error
number=[2,4,6,8]
try:
    print("the number ",number[5])
except IndexError:
    print("Invalid bound ans")    

# Using system
number=[2,4,6,8]
# try:
print("the number ",number[5])
  