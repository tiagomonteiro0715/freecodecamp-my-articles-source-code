class house():

    company_name = "Awesome building company"

    inflation_coefficient = 1.08

    def __init__(self, address, state, Alarm, price):
        self.address = address
        self.state = state
        self.Alarm = Alarm
        self.price = price

    def correctPriceMethod(self):
        self.price = self.price * self.inflation_coefficient

#-----------------------------------------------------------

apartement1 = house(1234, "california", False , 300000)
apartement2 = house(1234, "california", False , 300000)
apartement3Price = 300000

print(apartement1.price)

apartement1.correctPriceMethod()
print(apartement1.price)

#-----------------------------------------------------------

house.correctPriceMethod(apartement2)
print(apartement2.price)

#-----------------------------------------------------------

def correctPricefunction(apartement):
    return apartement * 1.08

print(apartement3Price)

apartement3Price = correctPricefunction(apartement3Price)
print(apartement3Price)
