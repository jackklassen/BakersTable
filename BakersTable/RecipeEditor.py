
import RecipeListdict as rl
class recipeeditor():
        def __init__(self):
                self.tempdict = dict()
                self.tempname = str()
                self.temprecipe = rl.recipelistdict.recipe()


        def setname(self,name):
                self.tempname = name

        def addtodict(self,key,value):
                self.tempdict[key] = value

        def deletefromdict(self,key):
                self.tempdict[key] = 0

        def showdict(self):
                print(self.tempname)
                print("___________________________")           
                for key,val in self.tempdict.items():
                        print(key, "       ", val,"g")


#save the edited recipe
        def saverecipe(self):
                self.temprecipe.setrecipename(self.tempname)
                for key,val in self.tempdict.items():
                        self.temprecipe.addtorecipe(key,val)
                return self.temprecipe