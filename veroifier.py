from statistics import mean , median , mode
def main():
    x = mean([2,3,1,2,3,4,5,5,6,2,3,4,5,3,1])
    print(f"Mean: {x}")
    y = median([2,3,1,2,3,4,5,5,6,2,3,4,5,3,1])
    print(f"Median:{y}")
    z = mode([2,3,1,2,3,4,5,5,6,2,3,4,5,3,1])
    print(f"Mode:{z}")
    if verifier(x , y ,z):
        print("Formula Median = 3 * Mean - 2 * Mode is correct")
    else:
        print("Formula Median = 3 * Mean - 2 * Mode fails")    
def verifier(x , y , z):
    return 3*y == 2 * x + 1 * z 
main()        

        
    
