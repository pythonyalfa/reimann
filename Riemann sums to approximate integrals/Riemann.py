'''
Created on Apr 20, 2020

'''


print("This is for number 3.")
print("")
b = float(input("What is b:"))
a = float(input("What is a:"))
n = float(input("What is n:"))
interval = (b - a) / n
print("The subinterval is", interval)

t = a
print("The left endpoints are: ")
while t < b:
    print(t)
    t += interval

print("Lets compute the Left Reimann sum. Assume F(x) = (x^2+2)")
t = 0
while a < b:
    t += ((1 / a) + 2)
    a += interval
print(t * interval)
