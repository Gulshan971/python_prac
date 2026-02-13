def main():
    x = input("Give  a string :")
    toggle(x)
def toggle(x = "World"):
     i = 0 
     n = len(x)
     y = ""
     while i < n : 
        y += x[n-i-1]
        i += 1
     print("Reversed String : ",y)
     if(y==x):
         print("Palindrome") 
     else:
         print("Not a palindrome")    
main()  
# print(dir(str))   