def main():
    x = int(input("Enter the value of x : "))
    print(is_even(x))
    if is_even(x):
        print("Even")
    else:
        print("odd")
# def is_even(x):
#     if x | 2 == 0 : 
#         return True         
def is_even(x):
    return True if x % 2 == 0  else False    
main() 