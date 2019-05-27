import recipeobject as recipeobject
class recipelist(object):

    def __init__(self):
        self.List = list()
        #create
    def addrecipe(self,recipe):
        self.List.append(recipe)

        #read
    def getrecipe(self,recipe):
        for x in self.List:
            if recipe.equals(x):
                return x
            else:
                return 0 

        #update
                

        #delete
        def deleterecipe(self,recipe):
            self.list.remove(recipe)
