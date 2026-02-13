# import sys 
# print(f"Hello , This side {sys.argv[2]}, Welcome to the world of python")
# # print("Hello, from Python to ",sys.argv[1])
"""import sys
if(len(sys.argv) < 2):
    sys.exit("Too few arguments")
elif(len(sys.argv) > 2):
    sys.exit("Too many arguments")
else:
    print("Welcome to" , sys.argv[1]) """
import sys
if len(sys.argv) < 2:
    print("Too few arguments")
for arg in sys.argv[1:-1:6]:
    print("Welcome" , arg , "to Python Community")           




