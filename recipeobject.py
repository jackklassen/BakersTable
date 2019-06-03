#An object to hold the nested dictionary
class recipe(object):
    def __init__(self):
        self.RecipeDict = dict()
        self.Recipename = str()
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
       self.Recipename = name


   
    def addsubrecipe(self,subrecipename):
       newrecipe = recipe()
       newrecipe.setrecipename(subrecipename)
       self.subrecipes.append(newrecipe)