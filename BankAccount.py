class BankAccount:
    #Initializatons for our bank management
    def __init__(self, acc_holder, init_bal=0):
        self.acc_holder=acc_holder
        self.bal=init_bal
    #Displays the balance
    def show_bal(self):
        print(f"Account Balance for {self.acc_holder}: ${self.bal:.2f}")
    #Function for depositing amount in bank account
    def deposit_amount(self, amt):
        if amt>0:
            self.bal+=amt
            print(f"Deposited Amount:${amt:.2f} into {self.acc_holder}'s account.")
            self.show_bal()
        else:
            print("Invalid deposit amount!! Please enter a correct value!!")
    #Function for money withdrawal from bank account
    def withdraw_money(self, amt):
        if 0<amt<=self.bal:
            self.bal-=amt
            print(f"Withdraw Amount:${amt:.2f} from {self.acc_holder}'s accouunt.")
            self.show_bal()
        else:
            print("Invalid withdrawl amount !!Check Balance and try again!!")
#Main function which takes the user inputs..
if __name__=="__main__":
    acc_holder=input("Enter account holder's name: ")
    init_bal=float(input("Enter initial balance: "))
    account=BankAccount(acc_holder, init_bal)
    while True:
        print("\nOptions:")
        print("1. Check Balance ")
        print("2. Make a Deposit")
        print("3. Make a Withdrawl")
        print("4.Exit")
        option=input("Enter your option(1-4): ")
        if option == '1':
            account.show_bal()
        elif option == '2':
            amt = float(input("Enter the amount to deposit: "))
            account.deposit_amount(amt)
        elif option == '3':
            amt = float(input("Enter the amount to withdraw: "))
            account.withdraw_money(amt)
        elif option == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose correct option..!!")