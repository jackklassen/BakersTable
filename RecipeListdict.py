
#todo:
#add an xml serializer method for all recipe
import re
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


        def tostring(self):
            for sub in self.subrecipes:
                sub.tostring()
            print("\n")
            print(self.recipename)
            print("___________________________")           
            for key,val in self.RecipeDict.items():
                print(key, "       ", val,"g")


        def setflourweight(self):
            for key,val in self.RecipeDict.items():
                if bool(re.search("flour",key)):
                    self.flourweight = val

        def savetoxml(self):

            root = ET.Element("recipe")
            for subrecipe in self.subrecipes:
                newsubdoc = ET.SubElement(root,subrecipe.recipename)
                for key,val in subrecipe.RecipeDict.items():
                   ET.SubElement(newsubdoc, key).text = val #cant send val as int must convert to string
                

            doc = ET.SubElement(root, "main")

            for key,val in self.RecipeDict.items():
                   ET.SubElement(doc, key).text = val

            tree = ET.ElementTree(root)
            tree.write("filename.xml")
            

        def loadfromxml(self):
            return 0