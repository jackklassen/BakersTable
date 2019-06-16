#import recipeobject as ro
import RecipeListdict as rl
import addrecipe as uh
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
test = rl.recipelistdict.recipe()
test2 = rl.recipelistdict.recipe()
test.setrecipename("test")
test2.setrecipename("test2")

test2.addtorecipe("water","100")
test.addtorecipe("flour","100")
test.addsubrecipe(test2)
test.savetoxml()

