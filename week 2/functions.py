# define a function which takes a name as a parameter
# put in some statements to execute - for now we can put in prints
# call the function

def greet(name):
    print ("This is a function")
    print ("This function is to say a greeting")
    print ("Hello " + name + "!")
greet("Neha")


# so we can have same function names with different parameters
# much like we can do in Java, this is called overloading
def greet():
    print ("This is a function")
    print ("This function is to say a greeting")
    print ("Hello!")
greet()

# we can also have multiple parameters
def greet(name, time_of_the_day):
    print ("This is a function")
    print ("This function is to say a greeting")
    print ("Hello " + name + ". " + time_of_the_day + "!")
greet("Neha", "Good Morning")
