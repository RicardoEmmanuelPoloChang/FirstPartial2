#STEP 1
def bodi():
  print ("Great in order to calculate your body mass index I need some information")
  print("First I´ll need your height in cm")
  height=input()
  print("and also your weight in kilos.")
  weight=input()
  bmi= int(weight)/(int(height)/100)**2
  print("Okay, then your BMI would be", bmi)
  if bmi<18.5:
    print("Oh, you are in the underweight range")
  elif 24.9>bmi>18.5:
    print("Congrats! You have a healthy weight!")
  elif 29.9>bmi>25:
    print("oh, you are considered to be overweight")
  elif bmi>30:
    print("Damn, you could be considered obese")
#STEP 2
bodi()
