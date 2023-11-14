# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}


#Nesting a list in the dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
print (travel_log)
print ("\n")

#Nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
print (travel_log)
print ("\n")


# nesting dictionary in a list
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
    },
]
print (travel_log)
print ("\n")
i = 0
while i < 5:
    print ("\n")
    i += 1

travel_log = []

def add_new_country(country, visits, list_of_cities):
    cities = []
    
    split_cities = list_of_cities.split(",")
    for(city) in split_cities:
        cities.append(city.strip())

    travel_log.append({"country": country, "visits": visits, "cities": cities})


country = input("What country did you visit? ")
visits = input("How many times did you visit? ")
list_of_cities = input("What cities did you visit? ")

add_new_country(country, visits, list_of_cities)

print(travel_log)