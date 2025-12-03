'''You’re developing an ATM withdrawal system. The user can:

Enter an amount to withdraw
Get an error if they enter invalid input (non-numeric or negative)
Get an error if they try to withdraw more than the balance
Always see a thank-you message, no matter what happens'''

def withraw(amount):
    balance_amount=2000
    if amount<=0 :
        raise ValueError("Only integer numbers should be entered ") 
    if amount <= balance_amount:
        print("amount is successfully debited")
        balance_amount= balance_amount-amount
        print("remaining balance:", balance_amount)
    else:
        print("total balance:",balance_amount, "Entered", amount ,"is not avaliable is account... try again")

        
try:
    user_input = input("Enter the amount to withdraw: ")
    amount = float(user_input)
    withraw(amount)
except ValueError:
    print("Invalid input! Please enter a valid numeric amount.")
finally:
    print("Thank you for using our ATM service.")
    
    
    