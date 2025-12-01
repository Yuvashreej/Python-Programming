# You’re building a basic banking system.
# There’s a global variable balance that stores the user’s total account balance. Inside a function,
# you perform a temporary calculation (like a test deposit) using a local variable, 
# which does not affect the actual balance unless updated globally.

# Create a global variable to store the account balance.
# Write a function that uses a local variable to simulate a change.
# Show how local changes don't affect the global value unless explicitly updated.


total_account_balance = 25000

# using local variable changes don't affect the global value

def test_deposit(amount):
    temp_total_account_balance = total_account_balance +amount   # Here temp_total_account_balance is local variable
    print("temporary calculation using local variable not affect the actual balance: ", temp_total_account_balance)
    
#  Explicity updating the actual/global value

def current_deposit(amount):
    global total_account_balance    #if we dont use global total_account_balance, 
    #python will consider "total_account_balance" as local variable which gives error.
    total_account_balance = total_account_balance +amount
    print("Explicitly updated the current/actual balance: ", total_account_balance)
    
    
temp=int(input("Enter amount to credit into your amount: "))

test_deposit(temp)
print("original/actual balance affected :",total_account_balance)
print('\n')

current_deposit(temp)
print("original/actual balance affected:",total_account_balance)

