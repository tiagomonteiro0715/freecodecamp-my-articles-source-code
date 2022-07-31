class house():
    def __init__(self, address, state, Alarm, price):
        self.address = address
        self.state = state
        self.Alarm = Alarm
        self.price = price


house1 = house(1234, "california", False , 300000)

house2 = house(5678, "texas", True , 100000)

print(house1.state)
print(house2.price)