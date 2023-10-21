## Item Class for formating how the data is to be represented and also holding the data
## about to be stored into the system's memory
class Item:

    def __init__(self, Number, Quantity, Name, Location, Description):

        self.Number = Number
        self.Quantity = Quantity
        self.Name = Name
        self.Location = Location
        self.Description = Description

    def __repr__(self):
        return '{},{},{},{},{}'.format(self.Number, self.Quantity, self.Name, self.Location, self.Description)