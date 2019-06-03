class MilkPackage:

    colour = "default"

    def __init__(self, manufacturer = "dafault", fatness = 0, volume = 0, amount_of_calories = 0, expiration_date = "0.0.0", presence_of_lactose = False, production_date = "0.0.0"):
        self.manufacturer = manufacturer
        self.fatness = fatness
        self.volume = volume
        self.amount_of_calories = amount_of_calories
        self.expiration_date = expiration_date
        self.presence_of_lactose = presence_of_lactose
        self.production_date = production_date

    def __del__(self):
        return "Deleted"

    def __str__(self):
        return str(self.__dict__)

    @staticmethod
    def printColour():
        return MilkPackage.colour

def main():

    milk_1 = MilkPackage(manufacturer="Molokia", fatness=25, amount_of_calories=1000, volume=100)
    milk_2 = MilkPackage(expiration_date="01.07.2019", presence_of_lactose=True, production_date="01.06.2019")
    milk_3 = MilkPackage(manufacturer="Halychuna", fatness=20, amount_of_calories=950, volume=500, expiration_date="09.07.2019", presence_of_lactose=False, production_date="04.06.2019")

    print(milk_1)
    print(milk_2)
    print(milk_3)
    print("kfdnkfn")

    MilkPackage.colour = "Green"

    print(MilkPackage.printColour())

if __name__ == '__main__':
    main()