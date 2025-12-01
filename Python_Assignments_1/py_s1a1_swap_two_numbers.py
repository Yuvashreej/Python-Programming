
# Program to swap two numbers without using temporary variable 

x= 123
y=456
print("Before swapping=",x,y)

x,y=y,x 

print ("After swapping =",x,y)

print("=====================")

# Program to swap two numbers using a temporary variable

# given numbers (locker codes)
a = 5
b = 10

print("Before swapping using temporary variable:")
print("a =", a)
print("b =", b)

# swap using a temporary variable
temp = a
a = b
b = temp

del temp 

print("After swapping using temporary variable:")
print("a =", a)
print("b =", b)









