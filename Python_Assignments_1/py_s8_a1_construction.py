'''-You’re building a system for an online movie ticket booking app. Every time a user books a ticket,
the system should store information like:

Movie name
Show time
Seat number
User name

Whenever a ticket is created, these details should be initialized automatically using a constructor.
Your job is to create a class called Ticket, and use a constructor (__init__ method in Python) 
to initialize ticket details when a new object is created.

Objective: 
Create a class with a constructor.
Use the constructor to initialize object attributes.
Create multiple ticket objects and display their details'''

class Ticket:
    
    def __init__(self,movie_name,show_time,seat_number,user_name):
        self.movie_name = movie_name
        self.show_time=show_time
        self.seat_number=seat_number
        self.user_name=user_name
        
    def movie_ticket_details(self):
        print("Ticket detials: ")
        print("user name: ", self.user_name)
        print("movie name: ", self.movie_name)
        print("showtime :",self.show_time)
        print("seatnumber: ",self.seat_number)
        
T1= Ticket("OG","7:30 PM","M4","Yuva")
T1.movie_ticket_details()

T2= Ticket("Vickram","11:30 AM","G7","Ranjith")
T2.movie_ticket_details()

t3 = Ticket("Aavesham", "5:00 PM", "B9", "charan")
t3.movie_ticket_details()


