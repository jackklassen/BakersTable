import RecipeListdict as rl
import addrecipe as ar




print("")
print("  _______ ")
print(" /       )")
print("/_____   | ")
print("(  '   )/ ")
print(" |.  '|/  ")
print(" |____|/  ")
print("Bakers Table")
print("=============")

def commandcheck(userinput):
    if userinput == "view all":
        print("viewing all")
    elif userinput == "help":
        print("viewing help")
    elif userinput == "view regex for any exixting things":
        print("viewing picked recipe")
    elif userinput == "add":
        addrecipe = ar.addrecipe()
        addrecipe.setupnewrecipe()

    

def isexit(userinput):
    if userinput == "exit":
        return True
    elif  userinput == "Exit":
            return True
    elif  userinput == "EXIT":
        return True
    elif  userinput == "E":
        return True
    elif  userinput == "e":
        return True
    else:
     return False
    

userinput = str()

while isexit(userinput) == False:
    userinput = input("Enter your command: ")
    commandcheck(userinput)