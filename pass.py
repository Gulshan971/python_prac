def main():
    x = get_int("What's x :")
    print(f"Value of x : {x}")
def get_int(prompt):
    while True:
        try:
            return  int(input(prompt))
        except ValueError:
            pass
main()        
