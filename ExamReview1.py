#STEP 1
def name():
  print("Wellcome To The converter, What currency do you have? pesos or dolars?")
  anser=input()
  if anser=="dollars":
    print("Then how many dollars do you have?")
  else:
    print("Too bad, we don´t recieve that, Tell me how many dollars you have?")
  number=input()
  result=int(number)*17.45
  print("Then you have", result ,"pesos.")
  result=int(number)*0.93
  print("or", result, "euros")
  result=int(number)*3246740
  print("and so you know, that would be", result, "venezuelan bolivars" )
#STEP 2 
name()
