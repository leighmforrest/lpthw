# create a mapping of stae to abbreviation
states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI",
}

# create a basic set of states and some cities in them
cities = {"CA": "San Francisco", "MI": "Detroit", "FL": "Jacksonville"}

# add some more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

# print out some cities
print("-" * 10)
print("NY State has: ", cities["NY"])
print("OR State has: ", cities["OR"])

# print some states
print("-" * 10)
print("Michigan's abbreviation is: ", states["Michigan"])
print("Florida's abbreviation is: ", states["Florida"])

# do it by using the state then cities dict
print("-" * 10)
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

# print every state abbreviation
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print("-" * 10)
# safely get a abbreviation by state that might not be there
state = states.get("Texas")

if not state:
    print("Sorry, no Texas.")


# get a city with a default value
city = cities.get("TX", "Does Not Exist")
print(f"The city for the state of 'TX' is: {city}")

# add to states
states["New Jersey"] = "NJ"
states["Pennsylvania"] = "PA"
states["Delaware"] = "DE"
states["Connecticut"] = "CT"

# add cities
cities["NJ"] = "Wildwood"
cities["PA"] = "Philadelphia"
cities["DE"] = "Rehobeth Beach"

print("-" * 10)

for state, abbrev in list(states.items()):
    print(f"The state of {state} is abbreviated {abbrev}")
    if cities.get(abbrev):
        print(f"and has city {cities[abbrev]}")
    else:
        print("and there is no city.")

print("-" * 10)
connecticut = states.get("Connecticut")
city = cities.get(connecticut, "No City")

print(f"The abbreviation of Connecticut is {connecticut}")
print(f"The city is {city}.")

states["Hawaii"] = "HI"
cities["HI"] = "Honolulu"

if "Hawaii" not in states:
    print("Hawaii is not in the states.")
else:
    print(f"The city of {states['Hawaii']} is {cities[states['Hawaii']]}.")

# copy cities dictionary
cities_copy = cities.copy()

print("-" * 10)
for state, city in cities_copy.items():
    print(f"The city of {state} is {city}")

print("-" * 10)

# display values of states
for abbrev in states.values():
    print(f"The abbreviation is {abbrev}.", end=" ")

    if abbrev in cities_copy:
        print(f"The city is {cities_copy[abbrev]}.")
    else:
        print("There is no city listed.")
