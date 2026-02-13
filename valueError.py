# try:
#     x = int(input("What's the value of x : "))
    
# except ValueError:
#     print("x is not a number")
# else:
#     print(f"x is {x}") 
def main():
    x = func()
    print(f"Value of X: {x}")

def func():   
    while True:
        try:
          x = int(input("Enter value of x : "))
        except ValueError:
           print("x is not a number")
        else:
           return x 
              
main()

               