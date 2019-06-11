#import recipeobject as ro
import RecipeListdict as rl
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
testobj = rl.recipelistdict.recipe()
testlst = rl.recipelistdict()


testobj.setrecipename("test")

testobj.addtorecipe("test",100)
testobj2 = rl.recipelistdict.recipe()
testobj2.addtorecipe("test2",150)
testobj2.setrecipename("test2")
testobj.addsubrecipe(testobj2)
testlst.addrecipe(testobj)

testobj3 = testlst.getrecipe("test")

print(testobj3.tostring())
testlst.listrecipes()