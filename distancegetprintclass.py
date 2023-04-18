'''
Write a Python class which has two methods get_distance and print_distance, get_distance 
accept a distance in kilometers from the user and print_distance print the distance in meter.
'''


class Distance:
    def get_distance(self):
        self.lnkm = int(input("Enter the distance in Kilometers: "))
        print("In Kilometers:", self.lnkm)

    def print_distance(self):
        lnim = self.lnkm * 1000
        print("In Meters:", lnim)


D = Distance()
D.get_distance()
D.print_distance()
