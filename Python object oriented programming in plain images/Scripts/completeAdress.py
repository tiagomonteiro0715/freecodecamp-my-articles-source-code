class house():
    def __init__(self, address, street , state):
        self.address = address
        self.street = street
        self.state = state

        self.completeAddress = str(address) + " " + state


house = house(1234, "california", "awesome road")

print(house.completeAddress)