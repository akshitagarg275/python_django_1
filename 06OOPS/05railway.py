'''
create a train class

book a seat
cancel a seat
get fare information
get status of seats available(no of seats)

Rajdhani Express
seats = [1,2,3,4,5]
fare = 50rs
'''

class Train :

    def __init__(self,name, noOfSeats, fare):
        self.name=name
        self.noOfSeats=noOfSeats
        self.fare = fare
        self.seats = list(range(1,self.noOfSeats+1))

    def getInfo(self):
        print(f"Name  of train is: {self.name}")
        print(f"fare of each seat is Rs.{self.fare}")
        print(f"no of seats available : {self.noOfSeats}")
        print(f"seats in train: {self.seats}")
    
    def bookASeat(self, no):
        if no > len(self.seats):
            print(f"Seats are not available . {no - len(self.seats)} seats can be booked")
        elif no < 1:
            print("Enter valid no of seats")
        else:
            for i in range(no):
                self.seats.pop(0)
            print(f"{no} seats are booked")
    
    def cancelSeat(self, seatNo):
        if seatNo <1 or seatNo > len(self.seats):
            print("Enter a valid seat no")
        
        elif seatNo in self.seats:
            print("This seat no is not allocated yet.")
        else:
            self.seats.append(seatNo)
            self.seats.sort()
            print(f"seat with seatno : {seatNo} , cancelled successfully")


t1=Train("RE" , 5 , 50)
t1.getInfo()
t1.bookASeat(2)
t1.cancelSeat(1)
t1.getInfo()



