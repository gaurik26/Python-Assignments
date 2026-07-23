def fun1():
    print("Inside fun1")

# function which accepts value and retuns nothing 
def fun2(value):
    print("Inside fun2")
    print("Accepted value is :", value)

# function which accepts value and returns value
def fun3(value):
    print("Inside fun3")
    print("Accepted value is :", value)
    return value + 10

# function which accepts multiple value and returns multiple value
def fun4(value1 , value2):
    print("Inside function")
    add = value1 + value2
    sub = value1 - value2
    return add,sub
print(fun4(10,5))

#Function which calls another function defined outside it .

def fun5():
    print("Inside fun5")
fun2(10)
fun5()

#Function which contains another nested function inside it.

def fun6():
    print("Inside fun6")
    def infun7():
        print("Inside fun7")
    infun7()
fun6()


no=11
fun1()
fun2(no)

ret = fun3(no)
print("Return value is: ",ret)

fun5()

ret1 , ret2 = fun4(10,4)
print("Addition is :",ret1)
print("Subtraction is :",ret2)




