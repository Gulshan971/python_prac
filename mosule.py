import sys
import practiceLib 
if len(sys.argv) < 2:
    print("Too few arguments")
else:
    practiceLib.hello(sys.argv[1])
    practiceLib.terminate(sys.argv[1])    