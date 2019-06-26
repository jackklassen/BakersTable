

import os
import re
import untangle
import xml.etree.cElementTree as ET


class recipelistdict(object):

    def __init__(self):
        self.dict = dict()
        #create
    def addrecipe(self,recipe):
        string = recipe.recipename
        self.dict[string] = recipe
        #print(self.dict[string])
        #read
    def getrecipe(self,recipename):
        return self.dict.get(recipename,"no recipe found.")

        #update
          #get recipe of the same name
          #and delete it then readd it     

        #delete
    def deleterecipe(self,recipename):
        recipe = self.getrecipe(recipename)
        self.dict.pop(recipe)

    ##List all names of Recipes in the recipe list
    def listrecipes(self):
        for key,val in self.dict.items():
            print(val.recipename)


    def savealltoxml(self):
        for r in self.dict.items():
            r.savetoxml()
    
    def loadallfromxml(self):
        path = "BakersTable/recipes"
        files = []
        for r, d, f in os.walk(path):
            for file in f:
                if '.xml' in file:
                    files.append(os.path.join(r, file))

        for f in files:
            newrecipe = recipelistdict.recipe()
            newrecipe.loadfromxml(f)
            self.addrecipe(newrecipe)
        

    class recipe:
        def __init__(self):
            self.RecipeDict = dict()
            self.recipename = str()
            self.subrecipes = list()
            self.flourweight = 0

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
            if self.isnumber(value):
                self.RecipeDict[key] = value
            else:
                return False

        def readfromrecipe(self,key):
            return self.RecipeDict[key]
   
        def setrecipename(self,name):
            self.recipename = name


   
        def addsubrecipe(self,subrecipe):
            self.subrecipes.append(subrecipe)

        def getsubrecipe(self,subrecipename):
            for s in self.subrecipes:
                if s.recipenam.equals(subrecipename):
                    return s
            return 0

        def getrecipename(self):
            return self.recipename

        def tostring(self):
            self.setflourweight()
            self.tostringrecursive()


        def tostringrecursive(self): ## the recursive part of tostring
            #self.flourweight = 200
            for sub in self.subrecipes:
                sub.flourweight = self.flourweight
                sub.tostringrecursive()
            print("\n")
            print(self.recipename)
            print("___________________________")           
            for key,val in self.RecipeDict.items():
                if self.isnumber(val):
                    if(self.flourweight != 0): 
                        bakerspercent = (int(val) / self.flourweight)
                    else:
                        bakerspercent = 0
                    print(key, "       ", val,"g","    ","{:.2%}".format(bakerspercent))
                else:
                    return False


    #sets the total weigt of the flour in a recipe to use in a bakers prcentage
        def setflourweight(self):
            for subrecipe in self.subrecipes:
                subrecipe.setflourweight()
            for key,val in self.RecipeDict.items():
                if "flour" in key.lower():
                    self.flourweight += int(val)
                    

        def isnumber(self,input):
            try:
                float(input)
                return True
            except ValueError:
                return False

                    

#################### Handle ALtering the recipe by dividing or multipying it ####################
        def multiplyrecipe(self,multivalue):
            for subrecipe in self.subrecipes:
                subrecipe.multiplyrecipe(multivalue)
            for key,val in self.RecipeDict.items():
                self.RecipeDict[key] = (int(val) * multivalue)

        def dividerecipe(self,dividevalue):
            for subrecipe in self.subrecipes:
                subrecipe.dividerecipe(dividevalue)
            for key,val in self.RecipeDict.items():
                 self.RecipeDict[key] = (int(val)/ dividevalue)
#################### /Handle ALtering the recipe by dividing or multipying it ####################


################################### XML Proccessing ###################################
        def savetoxml(self):

            root = ET.Element("recipe",attrib={"recipename":self.recipename})
           
            for subrecipe in self.subrecipes:
                newsubdoc = ET.SubElement(root,"subrecipe",attrib={"subrecipename":subrecipe.recipename})
               
                for key,val in subrecipe.RecipeDict.items():
                   ET.SubElement(newsubdoc,"ingredient",attrib={key:val}).text #cant send val as int must convert to string
                

            doc = ET.SubElement(root, "main")

            for key,val in self.RecipeDict.items():
                   ET.SubElement(doc,"ingredient",attrib={"name":key}).text = val

            tree = ET.ElementTree(root)
           
            filename = "BakersTable-master/recipes"+self.recipename + ".xml"
            tree.write(filename)
            

        def loadfromxml(self,xmlfile):
            #get names
            #for everything under subrecipe tag = key val = val
            #same for everything under main
            parser = untangle.parse(xmlfile)

            self.recipename = parser.recipe['recipename']
            if 'subrecipe' in dir(parser.recipe):
               for subrecipe in parser.recipe.subrecipe:
                
                   #############subrecipe processing#############
                   newsubrecipe = recipelistdict.recipe()

                   if subrecipe.get_attribute('subrecipename'):
                      newsubrecipe.setrecipename(subrecipe['subrecipename'])
                   for ingredient in subrecipe.ingredient:
                      newsubrecipe.addtorecipe(ingredient['name'],ingredient.cdata)
                   self.addsubrecipe(newsubrecipe)
                   #############/subrecipe processing#############

            for ingredient in parser.recipe.main.ingredient:
                self.addtorecipe(ingredient['name'],ingredient.cdata)
            ################################### XML Proccessing ###################################