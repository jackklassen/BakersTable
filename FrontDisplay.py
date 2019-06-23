import RecipeListdict as rl
import addrecipe as ar


recipelist =rl.recipelistdict()
    


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
        recipelist.loadallfromxml()
        recipelist.listrecipes()
    elif userinput == "help":
        print("viewing help")
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
    


def maindisplay():
    userinput = str()
    while isexit(userinput) == False:
        userinput = input("Enter your command: ")
        commandcheck(userinput)

maindisplay()