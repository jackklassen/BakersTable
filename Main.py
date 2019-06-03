#import recipeobject as ro
#tester

#recipe = ro.recipe()

#test = dict()
#name ="levain"
#test['Flour'] = 100
#test['Water'] = 100

#recipe.addtorecipe(name,test)


#recipe.addtorecipe("test",5)

#print(recipe.readfromrecipe("test"))
#print(recipe.readfromrecipe(name))
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