def main():
    n = freq_count()
    chirp(n) 

def chirp(n):
    if(n==0):
        return
    print("Chirp") 
    chirp(n-1)
    
def freq_count():
    x = int(input("Enter freq :"))
    while True : 
        if x > 0 : break 
        x = int(input("Enter frequency :"))
    return x  
main()     