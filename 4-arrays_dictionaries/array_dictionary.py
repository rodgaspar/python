# Arrays
cars = ["Monza","Golf","Renegade","Polo","Fusca"]

for car in cars:
    print(car)

print("---")
    
# Dictionary
person = {"name":"Paul","lastname":"Sunday","age":"30","occupation":"Writer"}

print(person)
print(person["name"])
print(person["lastname"])
print(person["age"])
print(person["occupation"])

print("---")

for chave in person:
    print(chave + ": " + person[chave])
