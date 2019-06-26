import argparse
import FrontDisplay

parser = argparse.ArgumentParser(description='Run commands on the Program.')


parser.add_argument('-v', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='View a Recipe.')
parser.add_argument('RecipeName', metavar='N', type=str,
                   help='Name of the recipe to view.')

args = parser.parse_args() 
name = args.RecipeName
FrontDisplay.ViewRecipe("test")