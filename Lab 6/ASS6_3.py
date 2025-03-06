class Converter:
    convert = {
        "inches": 0.0254,
        "feet": 0.3048,
        "yards": 0.9144,
        "miles": 1609.34,
        "kilometers": 1000,
        "meters": 1,
        "centimeters": 0.01,
        "millimeters": 0.001
    }
    def __init__(self, length, unit):
        self.length_meters = length * self.conversion_factors[unit]  # Convert to meters
    def inches(self):
        return self.length_meters / self.conversion_factors["inches"]
    def feet(self):
        return self.length_meters / self.conversion_factors["feet"]
    def yards(self):
        return self.length_meters / self.conversion_factors["yards"]
    def miles(self):
        return self.length_meters / self.conversion_factors["miles"]
    def kilometers(self):
        return self.length_meters / self.conversion_factors["kilometers"]
    def meters(self):
        return self.length_meters / self.conversion_factors["meters"]
    def centimeters(self):
        return self.length_meters / self.conversion_factors["centimeters"]
    def millimeters(self):
        return self.length_meters / self.conversion_factors["millimeters"]
val=int(input('Enter value : '))
print("\n1.inches","2.yards","3.meters","4.kilometers",sep="\n")
measure=input("Enter conversion unit : ")
c = Converter(val, measure)
print(c.feet())        
print(c.yards())       
print(c.meters())      
print(c.kilometers())  
