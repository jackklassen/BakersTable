import recipeobject as ro

recipe = ro.recipe()

recipe.addtorecipe("test",5)

print(recipe.readfromrecipe("test"))