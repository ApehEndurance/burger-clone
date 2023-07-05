name = "Endurance"
pin = 1234
account_balance = 250000

enter_pin= int(input("Enter your pin "))

if enter_pin == pin:
    print("welcome " + name)
    bank_activities = input("""
    A. Withdraw
    B. Transfer
    C. Deposit
    D. Airtime
    E. check account balance
    """)

    if bank_activities == "A":
        withdrawal = int(input("How much would you like to withdraw? "))
        new_balance = account_balance - withdrawal
        print("Your new account balance is " + str(new_balance))

    elif bank_activities == "B":
        transfer = int(input("How much will you like to tranfer? "))
        new_balance = account_balance - transfer
        print("Your new account balance is " + str(new_balance))

    elif bank_activities == "C":
        deposit = int(input("How much will you like to deposit"))
        new_balance = account_balance + deposit
        print("Your new account balance is " + str(new_balance))

    elif bank_activities == "D":
        airtime = int(input("How much airtime will you like to buy"))
        new_balance = account_balance - airtime
        print("Your new account balance is " + str(new_balance))

    elif bank_activities == "E":
        print("Your account balance is " + str(account_balance))

else:
    print("Incorrect pin")

