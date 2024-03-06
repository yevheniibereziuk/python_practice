# x = 26

#if x == 25:
 #   print("Yes you are right")
#else:
#    print("No you are wrong")

age = 7
if (age <=4):
    print("You are baby")
elif (age > 4 ) and (age < 12):
    print("You are kid")
elif (age>= 12) and (age <19):
    print("You are teenager")
else:
    print("You alre old")

print("-------END---------")

all_cars = ['chrusler', 'dacia', 'bmw', 'KIA', 'vw', 'seat', 'skoda', 'daewo', 'audi', 'ford', 'Chevrolett']
german_cars = ['bmw', 'vw', 'audi']

# if 'daewo' in  all_cars:
 #   print("Yes, the car name in the list")
# else:
#    print("Not in the list")

for xxx in  all_cars:
    if xxx in german_cars:
        print(xxx + " is German car")
  #  else:
 #       print(xxx + " is not German car")