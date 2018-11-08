"""
Assignment
-----------
Design and Implement a parking lot monitoring system using OOPs concepts in Python.
Imagine an parking lot with 20 parking spaces, where each parking space has an ID which is a natural number, starting with 1, 2, 3, ….upto 20. Parking space '1' is the one closest to the entrance.
The parking space can be in three sizes: small(10 parking spaces), medium(7 parking spaces) and large slots(3 parking spaces).
# Three types of vehicles are allowed to be parked in a parking space: motorcycle(small), car(medium) and bus(large)
# A motorcycle can be parked in any small, medium or large parking spaces.
# A car can be parked in either a medium slot or a large parking spaces.
# A bus can be parked only in a large parking space.
# When a user enters the parking lot, vehicle type and vehicle ID are noted and fed as input to our system
Our system should assign the vehicle to the nearest parking space available(if any parking space is available)
User should be given a printed ticket with the assigned parking spot ID and his vehicle ID
"""

"""
I'm Assuming Parking Space IDs:
1-10 are small parking slots
11-17 are medium parking slots
18-20 are large parking slots
"""

# to find free parking slot availablity
def free(id):
    if id==1:
        for i in range(0,20):
            if(parking_slot[i]==0):
                return(i)
    elif id==2:
        for i in range(10,20):
            if(parking_slot[i]==0):
                return(i)
    elif id==3:
        for i in range(17,20):
            if(parking_slot[i]==0):
                return(i)
    return(-1)

class vehicle:
    # instance attributes
    def __init__(self, vt, id):
        self.vehicle_type = vt
        self.vehicle_id = id
        if vt == "motorcycle":
            a=free(1)
            if a!=(-1):
                self.parking_id = a
        elif vt == "car":
            a=free(2)
            if a!=(-1):
                self.parking_id = a
        elif vt == "bus":
            a=free(3)
            if a!=(-1):
                self.parking_id = a
        else:
            self.parking_id = (-1)
            print("\rWarning: Cannot Allocate a Parking slot to this vehicle due to lack of availablity")
    # printing attributes
    def Print_Ticket(self):
        print("\r  PARKING TICKET\r================")
        print("Vehicle Type: ", self.vehicle_type)
        print("Vehicle ID: ", self.vehicle_id)
        if self.parking_id!=(-1):
            print("Parking slot alloted: ", self.parking_id)
        else:
            print("Parking slot unallocated")

# driver codes
if __name__ == '__main__':
    parking_slot=[]
    # 0 for free-slot and 1 for occupied
    for i in range(0,20):
        parking_slot.append(0)
    while(1):
        print("Enter the Vehicle ID: ")
        a = input()
        print("Enter the Vehicle ID: ")
        b = input()
        c = vehicle(a,b)
        c.Print_Ticket()
