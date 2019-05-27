import recipeobject as ro
#tester

recipe = ro.recipe()

test = dict()
name ="levain"
test['Flour'] = 100
test['Water'] = 100

recipe.addtorecipe(name,test)


recipe.addtorecipe("test",5)

print(recipe.readfromrecipe("test"))
print(recipe.readfromrecipe(name))