#STEP 1 
def dog():
  print("Hello, as a guide code, I´m going to calculate the velocity, average velocity,")
  print("average time and average acceleration of a 2 meter stride.")
  print("First I´ll need to calculate the velocity of 3, 2m walks, ")
  print("so I´ll need the time each one took, tell me the first one´s time in seconds")
  dash1=input()
  it1ac=2/int(dash1)
  print("The velocity of that iteration would be", it1ac, "meters per second," )
  print("now the second one")
  dash2=input()
  it2ac=2/int(dash2)
  print("The velocity of that iteration would be", it2ac, "meters per second,")
  print("Now let´s ")
  print("calculate the average velocity")
  averageV= (int(it1ac)+int(it2ac))/2
  print("Which thanks to the previous results we know that is", averageV, "meters per second")
  time= (int(dash1)+int(dash2))/2
  print("and the average time for the 2m stride would be", time, "seconds")
  print("And with all of that we can know average acceleration")
  aacceleration= int(averageV)/int(time)
  print("Which would be", aacceleration, "yes")
#STEP 2
dog()
