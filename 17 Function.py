def say_hello(person1, person2 = "The Director"):
    print("Hello " + person1 + ", how are you?" +person2 + " is waiting for you")


say_hello("Jane", "Tim")

def fahr2celsius(fahr):
    celsius = (5* (fahr - 32))/9
    return celsius

print ("Celsius: ", round(fahr2celsius(100),2))
print ("Kelvin: ", round(fahr2celsius(100)+ 273.5 ,2))
