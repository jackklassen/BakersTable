#import recipeobject as recipeobject
class recipelistdict(object):

    def __init__(self):
        self.dict = dict()
        #create
    def addrecipe(self,recipe):
        self.dict[recipe.recipename] = recipe
        #read
    def getrecipe(self,recipename):
        return self.dict.get(recipename,"")

        #update
          #get recipe of the same name
          #and delete it then readd it     

        #delete
        def deleterecipe(self,recipename):
            recipe = self.getrecipe(recipename)
            self.dict.pop(recipe)

        def listrecipes(self):
            for x in self.dict:
                print(x.recipename)

    class recipe:
        def __init__(self):
            self.RecipeDict = dict()
            self.recipename = str()
            self.subrecipes = list()

        def checkhaskey(self,key):
            if key in self.RecipeDict.keys():
                return True
            else:
                return False


        def checkhasvalue(self,value):
            if value in self.RecipeDict.values():
                return True
            else:
                return False

        def addtorecipe(self,key, value):
            self.RecipeDict[key] = value

        def readfromrecipe(self,key):
            return self.RecipeDict[key]
   
        def setrecipename(self,name):
            self.recipename = name


   
        def addsubrecipe(self,subrecipename):
            newrecipe = recipelistdict.recipe()
            newrecipe.setrecipename(subrecipename)
            self.subrecipes.append(newrecipe)