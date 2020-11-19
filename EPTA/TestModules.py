##choice = input("What is your import choice?")
##choice = int(choice)
##print(choice)

choice = 1

if choice == 1:  
    import printT as printTee  
else:
    import printT2 as printTee

# printT is imported as printTee

modules = dir()
print(modules)

printTee.printT("chickens are my frint")

# that should print

import printT2 as printTee  # so he're we're seeing the overwriting of the module variable


modules = dir()
print(modules)

printTee.printT2("chickens are my frint")


print(printTee)

# want to do dynamic imports
# https://realpython.com/python-import/#dynamic-imports
# using 

# Whether game unloading or loading works will heavily depend on if the object serialization cares

