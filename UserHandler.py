#used to handle interattion between the user and the recipes
#todo clean up
#bug test and add better testable handelers for user inputs
import RecipeEditor as re
import RecipeListdict as rl
class userhandler():
    def __init__(self):
        self.recipes = rl.recipelistdict()
        self.newrecipe = object()
        self.newrecipename = str()
    def setupnewrecipe(self):
        self.newrecipe = rl.recipelistdict.recipe()
        #add a check if untitled already exists
        self.newrecipename = "Untitled"
        self.newrecipe.setrecipename(self.newrecipename)
        editingrecipe = True
        while editingrecipe == True:
            userinput = input("do you want to add a preferment/subrecipe?\n")

            if userinput == "yes":
                self.addpreferment()
            elif userinput == "no":
                self.addtorecipe()

            if userinput == "end": #or any other exit condiciton
                editingrecipe = False

    def addpreferment(self):
        editingpreferment = True
        userinput = ""
        newsubrecipe = rl.recipelistdict.recipe
        prefermentname = "untitled pre ferment" #same process as above for untitiled
        print("enter the ingredient and ammounts in grams in the command line.")
        while editingpreferment == True:
            userinput = input("")
            if userinput == "done":
                editingpreferment = False
        self.handlerecipeadding(prefermentname,userinput)
        #at the end of the while loop add the subrecipe to recipe
        self.newrecipe.addsubrecipe(newsubrecipe)


    def addtorecipe(self):
        addingtorecipe = True
        userinput = ""
        print("enter the ingredient and ammounts in grams in the command line and type view to see the currently added ingredients")
        while addingtorecipe == True:
            userinput = input("")
            if userinput == "done":
                addingtorecipe = False

        self.handlerecipeadding(self.newrecipename,userinput)
   


    def handlerecipeadding(self,recipename,userinput):
        return 0
        #regex problem
        #ex if no # then not an ingriendt ammount pair but if type 00 flour it is still just an ingredent
        #if recipe name is main recipe handle adding to that if not
        #add to subrecipe with the the recipename given
        #if userinput is ingrident amount split and add as key and value
        #if userinput is just ingredient then add as 0g and prompt the user to add and ammount

    #check if a untitled name alrady exist if yes return a new untitled name
    def checkuntitledname(self,givenlist):
        outputname = "untitled"
        addednumber = 1
        for x in givenlist:
            if x.recipename == outputname:# untitled or untitled(n) add a new
                outputname = outputname+addednumber
                addednumber = addednumber + 1
        return outputname