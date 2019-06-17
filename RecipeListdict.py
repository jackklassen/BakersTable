
#todo:
#add an xml serializer method for all recipe
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
        print(self.dict[string])
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

    def listrecipes(self):
        for x in self.dict:
            if x != str():
                print(x.recipename)


    def savealltoxml(self):
        for r in self.dict.items():
            r.savetoxml()
    
    def loadallfromxml(self):
        #https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
        return 0

    class recipe:
        def __init__(self):
            self.RecipeDict = dict()
            self.recipename = str()
            self.subrecipes = list()
            self.flourweight = int()

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
            #self.setflourweight()
            self.flourweight = 200
            for sub in self.subrecipes:
                sub.tostring()
            print("\n")
            print(self.recipename)
            print("___________________________")           
            for key,val in self.RecipeDict.items():
                bakerspercent= (int(val) / self.flourweight)
                
                print(key, "       ", val,"g","    ","{:.2%}".format(bakerspercent))


        def setflourweight(self):
            for key,val in self.RecipeDict.items():
                if bool(re.search("flour",key)):
                    self.flourweight = val

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
           
            filename = self.recipename + ".xml"
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

               
                        

            return 0