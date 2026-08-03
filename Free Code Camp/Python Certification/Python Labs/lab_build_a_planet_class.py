# Lab: Build a Planet Class
# I implemented a `Planet` class with an `__init__` method that validates its arguments, ensuring they are non-empty strings. I also added an `orbit` method and a custom `__str__` method, then created three planet instances and printed their details

class Planet:
    def __init__(self, name, planet_type, star):
        
        attributes = [name, planet_type, star]

        for attribute in attributes:
            if not isinstance(attribute, str):
                raise TypeError("name, planet type, and star must be strings")
        
        for attribute in attributes:
            if not attribute:
                raise ValueError("name, planet_type, and star must be non-empty strings")
        
        self.name = name
        self.planet_type = planet_type
        self.star = star
    
    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

planet_1 = Planet("Mars", "Rocky", "Sun")
planet_2 = Planet("Earth", "Rocky", "Sun")
planet_3 = Planet("Jupter", "Gas", "Sun")

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())