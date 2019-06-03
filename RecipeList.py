import recipeobject as recipeobject
class recipelist(object):

    def __init__(self):
        self.List = list()
        #create
    def addrecipe(self,recipe):
        self.List.append(recipe)

        #read
    def getrecipe(self,recipename):
        for x in self.List:
            if recipename.equals(x.recipename):
                return x
            else:
                return 0 

        #update
          #get recipe of the same name
          #and delete it then readd it     

        #delete
        def deleterecipe(self,recipename):
            recipe = self.getrecipe(recipename)
            self.list.remove(recipe)

        def listrecipes(self):
            return self.list.list()