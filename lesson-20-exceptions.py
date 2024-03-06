import sys
filename = "listofname.txt"



# myfile = open(filename, mode='r', encoding='Latin_1')
# print(myfile.read())
while True:
    try:
        print("Inside TRY")
        myfile = open(filename, mode='r', encoding='Latin_1')
    except Exception:
        print("inside EXCEPT")
        print("Error Found")
        print(sys.exc_info() [1])
        filename = input("Enter correct file name : ")
    else:
        print("Inside ELSE")
        print(myfile.read())
        sys.exit()
    finally:
        print("Inside Finally")
        print("===========EOF============")