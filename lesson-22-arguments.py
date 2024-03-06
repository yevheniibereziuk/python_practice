import sys
import os

#print("Hello")

#print(sys.argv[1:])
#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "/?":
        print("Help requested")
        print("Usage of this progreamm is: python.exe myfile.py")
    print("Arguments entered: " + str(sys.argv[1:]))
else:
    print("Arguments not provided")


os.system("ls > test.txt")
#os.mkdir("my dir")
sys.exit(2)





