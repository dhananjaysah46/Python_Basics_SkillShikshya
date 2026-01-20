def my_fuction(x):
    print("4")
    print("The number is:", x)


def my_decorator(some_function, num):
    def wrapper(num):
        print("1")
        print("inside wrapper to check even or odd number")

        if num%2 == 0:
            print("2")
            ret = "Even!"
        else:
            print("3")
            ret = "Odd!"
        some_function(num)
        print("5")
        return ret
    print("wrapper fuction is called")
    return wrapper
no =10
my_fuction = my_decorator(my_fuction, no)
print("Its", my_fuction(no))