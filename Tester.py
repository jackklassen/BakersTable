#import recipeobject as ro
import RecipeListdict as rl
import addrecipe as uh
import untangle as ut
#tester

#recipe = ro.recipe()

#test = dict()
#name ="levain"
#test['Flour'] = 100
#test['Water'] = 100

#recipe.addtorecipe(name,test)


#recipe.addtorecipe("test",5)

#print(recipe.readfromrecipe("test"))
#print(recipe.readfromrecipe(name))
#testobj = rl.recipelistdict.recipe()
#testlst = rl.recipelistdict()


#testobj.setrecipename("test")

#testobj.addtorecipe("test",100)
#testobj2 = rl.recipelistdict.recipe()
#testobj2.addtorecipe("test2",150)
#testobj2.setrecipename("test2")
#testobj.addsubrecipe(testobj2)
#testlst.addrecipe(testobj)

#testobj3 = testlst.getrecipe("test")

#print(testobj3.tostring())
#testlst.listrecipes()
#obj = uh.addrecipe()

#obj.setupnewrecipe()
#test = rl.recipelistdict.recipe()
#test2 = rl.recipelistdict.recipe()
#test.setrecipename("test")
#test2.setrecipename("test2")

#test2.addtorecipe("water","100")
#test.addtorecipe("flour","100")
#test.addsubrecipe(test2)
#test.savetoxml()

#test.tostring()

#obj = ut.parse("test.xml")

#dir(obj.recipe)
#if 'subrecipe' in dir(obj.recipe):
  #  for subrecipe in obj.recipe.subrecipe:
   #     if subrecipe.get_attribute('subrecipename'):
   #         print(subrecipe['subrecipename']) # Prints 123
   #     
  #      for ingredient in subrecipe.ingredient:
    #        print(ingredient['name'])
   #         print(ingredient.cdata)
            
testrec = rl.recipelistdict.recipe()

testrec.loadfromxml("test.xml")
#print(testrec.RecipeDict)
testrec.tostring()

#print(obj.recipe.subrecipe)

#print(obj.recipe.subrecipe)

parser = ut.parse("test.xml")
print(parser.recipe['recipename'])
if 'subrecipe' in dir(parser.recipe):
    for subrecipe in parser.recipe.subrecipe:
                
                   #############subrecipe processing#############
       

        if subrecipe.get_attribute('subrecipename'):
            print(subrecipe['subrecipename'])
        for ingredient in subrecipe.ingredient:
               print(ingredient['name'],ingredient.cdata)
        #
                   #############/subrecipe processing#############

for ingredient in parser.recipe.main.ingredient:
    print(ingredient['name'],ingredient.cdata)