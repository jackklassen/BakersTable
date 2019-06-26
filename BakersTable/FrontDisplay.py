import RecipeListdict as rl
import addrecipe as ar


recipelist =rl.recipelistdict()
recipelist.loadallfromxml()
viewedrecipe = rl.recipelistdict.recipe()
    


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
    HandleCommand = {
        "view all":ViewAll,
        "help":ViewHelp,
        "add": AddRecipeFront,
        "view":ViewRecipe,
        "multiply": multiplyrecipefront,
        "divide": dividerecipefront
    }.get(userinput.lower(),default)()

def ViewAll():
     recipelist.listrecipes()

def ViewHelp():
    print("viewing help")

def AddRecipeFront():
    addrecipe = ar.addrecipe()
    addrecipe.setupnewrecipe()

def ViewRecipe(newinput = "none"):
    if newinput == "none":
        newinput = input("Name the Recipe to view: ")
    viewedrecipe = recipelist.getrecipe(newinput)
    print(viewedrecipe.tostring())


def multiplyrecipefront(newinput = "none"):
        if newinput == "none":
                newinput = input("Multiply the recipe by what ammount: ")
        viewedrecipe.multiplyrecipe(newinput)

def dividerecipefront(newinput = "none"):
    if newinput == "none":
        newinput = input("Multiply the recipe by what ammount: ")
    viewedrecipe.dividerecipe(newinput)
    
def default():
    print("")

def isexit(userinput):
    isexit={
        "exit": True,
        "Exit": True,
        "EXIT": True,
        "E": True,
        "e": True
        }
    return isexit.get(userinput,False)
    
    


def maindisplay():
    userinput = str()
    while isexit(userinput) == False:
        userinput = input("Enter your command: ")
        commandcheck(userinput)

maindisplay()