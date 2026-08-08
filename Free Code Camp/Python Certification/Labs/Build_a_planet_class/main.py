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