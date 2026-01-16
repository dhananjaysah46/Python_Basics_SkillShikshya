# Demonstrating that function arguments in Python are passed by object reference
def testFuction(arg):
    print("Id inside the function:", id(arg))
    arg = arg + 1
    print("new object after increment:", arg, id(arg))
var = 10
print("Id before passing to function:", id(var))
testFuction(var)
print("Id after function call:", var)
