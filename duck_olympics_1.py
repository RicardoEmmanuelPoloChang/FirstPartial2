def suma (a,b):
  x= a+b
  return x

def resta(a,b):
  x= a-b
  return x

print("Dame el primer numero")
a = int(input())
print("Dame el segundo numero")
b = int(input())
print("la suma de", suma(a,b), "y la resta ", resta(a,b))

def multiplication (a,b):
  x= a*b
  return x

def division (a,b):
  x= a/b
  return x

print("give me number")
a= int(input())
print("another one")
b= int(input())
print("multiplication is", multiplication(a,b), "and division is", division (a,b))



def conversion(kilo):
    x= kilo*100
    return x

print("Give me a distance in kilometers")
kilo= int(input())

print("that would be", conversion(kilo), "meters")


def triangle(b,h):
  x= (b*h)/2
  return x
print("gime the base of your triangle")
b=int(input())
print("now da height")
h=int(input())
print("The area f your triangle is", triangle(b,h))
