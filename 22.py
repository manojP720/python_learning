names = [ "Alice", "Bob", "Charlie", "David", "Eve" ]

d = {name  : len(name )for name in names }
print(d)


city_population = { "New York" : 8000000, "Los Angeles" : 4000000, "Chicago" : 2700000 }

large_cities = { city : population for city, population in city_population.items() if population > 3000000 }