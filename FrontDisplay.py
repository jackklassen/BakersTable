import recipeobject as robject
import RecipeList as rlist


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

#while isexit(userinput) == False:
  #  userinput = input("Enter your command: ")
  #      commandcheck(userinput)


#def commandcheck(self,userinput):
 #   if userinput == "view all":