import argparse
import FrontDisplay as fd
import RecipeListdict as rl

display = fd.FrontDisplay()

recipelist = rl.recipelistdict()
recipelist.loadallfromxml()
recipe = rl.recipelistdict.recipe()

parser = argparse.ArgumentParser(description='Run commands on the Program.')


parser.add_argument('-v',help='View a Recipe.', dest="view",action = "store",type = str)

parser.add_argument('-va', help='View all Recipes.', dest="viewall",action = "store_true")

parser.add_argument('-m', help='Multiply a Recipe.' ,dest="multiply",action = "store",type = float) 

parser.add_argument('-d',   help='Divide a Recipe.',dest="divide",action = "store",type = float)
            


args = parser.parse_args()

if args.view:

    if args.multiply:
           display.setviewedrecipe(args.view)
           display.multiplyrecipefront(args.multiply)
           display.ViewRecipe(args.view)
           

    if args.divide:
           display.setviewedrecipe(args.view)
           display.dividerecipefront(args.multiply)
           display.ViewRecipe(args.view)
    else:
        display.setviewedrecipe(args.view)       
        display.ViewRecipe(args.view)
           

if args.viewall:
    display.ViewAll()
    
else:
    display.maindisplay()

