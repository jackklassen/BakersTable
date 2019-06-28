#used to handle interattion between the user and the recipes
#todo clean up
#bug test and add better testable handelers for user inputs
import RecipeEditor as re
import RecipeListdict as rl
class addrecipe():
    def __init__(self):
        self.recipes = rl.recipelistdict()
        self.newrecipe = object()
        self.newrecipename = str()
        self.newsubrecipe = object()

    def setupnewrecipe(self):
        self.newrecipe = rl.recipelistdict.recipe()
        #add a check if untitled already exists
        self.newrecipename = "Untitled"
        self.newrecipe.setrecipename(self.newrecipename)
        editingrecipe = True
        while editingrecipe == True:
            userinput = input("do you want to add a preferment/subrecipe? type done when you are finished.\n")


            if userinput == "yes":
                self.addpreferment()
            elif userinput == "no":
                self.addtorecipe()

            elif userinput == "done":
                self.saverecipe()
                editingrecipe = False

            if userinput == "e": #or any other exit condiciton
                #save the list in a file
                self.saverecipe()
                editingrecipe = False

    def addpreferment(self):
        editingpreferment = True
        userinput = ""
        self.newsubrecipe = rl.recipelistdict.recipe()

        prefermentname = "untitled pre ferment" #same process as above for untitiled
        prefermentname = input("enter the subrecipe name.\n")
        self.newsubrecipe.setrecipename(prefermentname)

        
        while editingpreferment == True:
            print("enter the ingredient name.")
            userinput = input("")
            
            if userinput == "done":
                editingpreferment = False
                continue
            self.handlesubrecipeadding(userinput)
        #at the end of the while loop add the subrecipe to recipe
        self.newrecipe.addsubrecipe(self.newsubrecipe)


    def addtorecipe(self):
        addingtorecipe = True
        userinput = ""
        
        while addingtorecipe == True:
            print("enter the ingredient name.")
            userinput = input("")
            
            if userinput == "done":
                #save save object into the list
                addingtorecipe = False
                continue
            self.handlerecipeadding(userinput)
        
   

    def handlesubrecipeadding(self, userinput):
        key = userinput
        value = input("enter the ammount in grams.\n")
        #tempdata = userinput.split(",")
        self.newsubrecipe.addtorecipe(key,value)


    def handlerecipeadding(self, userinput):
        key = userinput
        value = input("enter the ammount in grams.\n")
        #tempdata = userinput.split(",")
        return self.newrecipe.addtorecipe(key,value)

        
    def checkuntitledname(self,givenlist):
        outputname = "untitled"
        addednumber = 1
        for x in givenlist:
            if x.recipename == outputname:# untitled or untitled(n) add a new
                outputname = outputname+addednumber
                addednumber = addednumber + 1
        return outputname

    def saverecipe(self):
        inputname = input("Name of new recipe: ")
        self.newrecipe.setrecipename(inputname)
        self.newrecipe.savetoxml()
        print("recipe " + self.newrecipe.recipename+ " saved.")
        