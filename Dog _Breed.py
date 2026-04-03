class Dog:

    species = "Animal"

    # instance attribute
    def __init__(self, Breed, Colour)  :    
        self.Breed = Breed
        self.Colour = Colour

# instantiate the Parrot class
Golden_Retriever = Dog("Golden_Retriever", Golden)
German_Shephard = Dog("German_Shephard", Black_White)

# access the class attributes
print("Golden_Retriever is a {}".format(Golden_Retriever.species))
print("German_Shephard is also a {}".format(German_Shephard.species))

# access the instance attributes
print("{} is {} years old".format( Golden_Retriever.Breed, Golden_Retriever.Colour))
print("{} is {} years old".format( German_Shephard.Breed, German_Shephard.Colour))