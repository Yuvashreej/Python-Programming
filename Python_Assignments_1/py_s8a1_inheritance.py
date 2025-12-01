'''Salary Management System using Object-Oriented Programming with inheritance, 
involving Employee and Manager classes.

Scenario:
You're creating a salary management program for a company. There are two types of people:

Employees: Have basic details like name, ID, and base salary.

Managers: Are also employees but get additional bonuses and perks.'''


class Employee:
    def __init__(self,name,id,base_salary):
        self.name=name
        self.id=id
        self.base_salary=base_salary
        
    def salary(self):                                         # parent method gets inherited by child class
        print("salary is :", self.base_salary)
    
    def show_details(self):
        print("employee details: ", self.name, self.id, self.base_salary)
        
class Manger(Employee):
    def __init__(self, name, id, base_salary,bonuses,perks):
        super().__init__(name, id, base_salary)                # calling parent constructor 
        self.bonuses=bonuses
        self.perks=perks
        
    def show_details(self):                                     # Method overriding 
        print("Manger details: ", self.name, self.id, self.base_salary,self.bonuses,self.perks)
        

E1=Employee("yuva",10001,15000)
E1.show_details()
E1.salary()

E2=Employee("charan",10002,20000)
E2.show_details()
E2.salary()


M1=Manger("ranjith",10003,25000,15000,5000)
M1.show_details()
M1.salary()   # Parent class method, called by child class

        
    
    


