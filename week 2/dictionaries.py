programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

print(f"Print dictionary value -> {programming_dictionary['Loop']}")

print("\n")


#Adding a new item in the dictionary and print all the values
programming_dictionary["Variable"] = "A placeholder for data."
print(f"Print dictionary -> {programming_dictionary}")


print("\n")

#rewrite a value in the dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(f"Print dictionary -> {programming_dictionary}")

print("\n")

#loop through a dictionary
print("Here are all the keys and values after we have looped thru it.")
for key in programming_dictionary:
    print(f"Print dictionary key -> {key}")
    print(f"Print dictionary value -> {programming_dictionary[key]}")

print("\n")

#wipe the dictionary
programming_dictionary = {}
print(f"Print dictionary -> {programming_dictionary}")