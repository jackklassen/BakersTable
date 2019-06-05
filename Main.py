#import recipeobject as ro
import RecipeListdicttest as rl
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

testlst.addrecipe(testobj)

print(testlst.getrecipe("test"))
