"""x = int(input("What's the value of x :"))
y = float(input("What's the value of y:"))
z = round(x + y)
print(f"{x/y:,.6f}")"""
"""
without type casting it concatenates the two variables and using that gives the exact answer 
"""
def main():
    x = (input("Enter the vlaue of x :"))
    z = modulo(x)
    print(f"the modulo of {x} is {z}")

def modulo(x):
    if x < 0 :
        return -1 * x 
    return x

if __name__ == "__main__":
   main()