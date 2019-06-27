import RecipeListdict as rl
import addrecipe as ar

class FrontDisplay():
        def __init__(self):
                self.recipelist =rl.recipelistdict()
                self.recipelist.loadallfromxml()
                self.viewedrecipe = rl.recipelistdict.recipe()
                print("")
                print("  _______ ")
                print(" /       )")
                print("/_____   | ")
                print("(  '   )/ ")
                print(" |.  '|/  ")
                print(" |____|/  ")
                print("Bakers Table")
                print("=============")






        def commandcheck(self,userinput):
                HandleCommand = {
                "view all":self.ViewAll,
                "help":self.ViewHelp,
                "add": self.AddRecipeFront,
                "view":self.ViewRecipe,
                "multiply": self.multiplyrecipefront,
                "divide": self.dividerecipefront
                }.get(userinput.lower(),self.default)()

        def ViewAll(self):
                self.recipelist.listrecipes()

        def ViewHelp(self):
                print("viewing help")

        def AddRecipeFront(self):
                addrecipe = ar.addrecipe()
                addrecipe.setupnewrecipe()

        def ViewRecipe(self,newinput = "none",alter = "none",ammount= ""):
                if newinput == "none":
                        newinput = input("Name the Recipe to view: ")
                        

                self.viewedrecipe.tostring()
               

        def setviewedrecipe(self,newinput = "none"):
                if newinput == "none":
                        return False
                self.viewedrecipe = self.recipelist.getrecipe(newinput)
                return self.viewedrecipe


        def multiplyrecipefront(self,newinput = "none"):
                if newinput == "none":
                        newinput = input("Multiply the recipe by what ammount: ")
                self.viewedrecipe.multiplyrecipe(newinput)
                

        #ViewRecipe(newinput)
        

        def dividerecipefront(self,newinput = "none"):
                if newinput == "none":
                        newinput = input("Multiply the recipe by what ammount: ")
                self.viewedrecipe.dividerecipe(newinput)
    
        def default(self):
                print("")

        def isexit(self,userinput):
                isexit={
                "exit": True,
                "Exit": True,
                "EXIT": True,
                "E": True,
                "e": True
                }
                return isexit.get(userinput,False)
    
    


        def maindisplay(self):
                userinput = str()
                while self.isexit(userinput) == False:
                        userinput = input("Enter your command: ")
                        self.commandcheck(userinput)

#maindisplay()