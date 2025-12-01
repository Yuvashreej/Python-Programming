
def Assign_gates(TicketNo):
    if TicketNo%2 == 0:
         return "Gate A"
    else:
         return "Gate B"

TicketNo = int(input("Enter ticket number"))
Result = Assign_gates(TicketNo)
print("you should enter form :", Result)
     

